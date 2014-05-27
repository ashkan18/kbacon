import os
from services import artists_services
from helpers.json_helper import jsonify_artist_model

__author__ = 'Ashkan'

from flask import Flask, jsonify, request

app = Flask(__name__)
app.debug = True

# log to stderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)

@app.route('/api/artists/', methods=['GET'])
def get_all_artists():
    """
    This interface returns the list of artists with the query string in their name
    sample curl:
        curl -X GET http://localhost:999/artists/
    """
    return jsonify(artists=artists_services.get_all_artists())


@app.route('/api/artists/search/', methods=['GET'])
def search_artists():
    query = request.args['query']
    search_results = artists_services.search_artists(query)
    json_result = []
    for actor in search_results:
        json_result.append(jsonify_artist_model(actor))
    return jsonify(artists=json_result)


@app.route('/api/artists/<string:artist_name>', methods=['GET'])
def find_path(artist_name):
    app.logger.info("hi")
    path = artists_services.find_path_between_artists(artist_name)
    return jsonify(path=path)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
