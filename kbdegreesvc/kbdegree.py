import os
from flask import Flask, jsonify, request

from kbdegreesvc.services import artists_services
from kbdegreesvc.helpers.json_helper import jsonify_artist_model

__author__ = 'Ashkan'


# create a new flask application
app = Flask(__name__, static_folder='{0}/../static'.format(os.path.dirname(__file__)))
app.debug = True

# log to stderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)

@app.route('/api/artists/search/', methods=['GET'])
def search_artists():
    """
    This method will search for artists in our data and return a list of artist who their name
    matches the input search query

    curl sample:
        http://localhost:5000/api/artists/search?query=sean

    @return: json list of artists matched this search query
    """
    query = request.args['query']
    search_results = artists_services.search_artists(query)
    json_result = []
    for artist in search_results:
        json_result.append(jsonify_artist_model(artist))
    return jsonify(artists=json_result)


@app.route('/api/artists/<artist_id>', methods=['GET'])
def find_path(artist_id):
    """
    This method will search for paths between requested artist and Kevin Bacon,
    if there is no path it will return empty path otherwise, it will return an ordered
    list showing the path from input artist to Kevin Bacon, a path is a combination of artists and films


    curl sample:
        http://localhost:5000/api/artists/57e379d456c58ed96b6673eab7730308dc08c582


    @param artist_id: String id of the artist we are looking for
    @return: json path which is a list of artists and films
    """
    app.logger.info(u"Get artist info by name: {0}".format(artist_id))
    path = artists_services.find_path_between_artists(artist_id)
    artist_model = artists_services.get_artist_by_id(artist_id)
    return jsonify(path=path, artist_name=artist_model.info['name'])


@app.route('/api/artists/', methods=['GET'])
def get_all_artists():
    """
    This interface returns the list of artists with the query string in their name
    sample curl:
        curl -X GET http://localhost:999/api/artists/
    """
    return jsonify(artists=artists_services.get_all_artists())


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


if __name__ == '__main__':
    # in case we want to run this locally, mostly for debug reasons
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
