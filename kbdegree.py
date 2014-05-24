import base64
import hmac
import os
import time
import urllib
import hashlib
from services import catalog_service, item_service

__author__ = 'Ashkan'

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/catalog/', methods=['GET'])
def get_current_catalog():
    """
    This interface returns the current issue of the catalog
    sample curl:
        curl -X GET http://localhost:999/catalog/
    """
    current_catalog = catalog_service.get_current_catalog()
    return jsonify(catalog=current_catalog)

@app.route('/catalog/items/<int:catalog_id>', methods=['GET'])
def get_catalog_items(catalog_id):
    items = item_service.get_items_for_catalog(catalog_id)
    return jsonify(items=items)


@app.route('/sign_s3/')
def sign_s3():
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET = os.environ.get('S3_BUCKET')

    object_name = request.args.get('s3_object_name')
    mime_type = request.args.get('s3_object_type')

    expires = int(time.time()+10)
    amz_headers = "x-amz-acl:public-read"

    put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

    signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request, hashlib.sha1).digest())
    signature = urllib.quote_plus(signature.strip())

    url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

    return jsonify(signed_request='%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' %
                                  (url, AWS_ACCESS_KEY, expires, signature),
                   url=url)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
