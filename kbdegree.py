import os

__author__ = 'Ashkan'

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/people/', methods=['GET'])
def get_all_people():
    """
    This interface returns the list of people with the query string in their name
    sample curl:
        curl -X GET http://localhost:999/people/
    """
    return jsonify(people={[{'name':'ashkan', 'movies':['rain', 'dar an sooy']},
                            {'name': 'nasseri', 'movies': ['estop']}]})


@app.route('api/people/search/', methods=['GET'])
def search_people():
    return jsonify(people={[{'name':'ashkan', 'movies':['rain', 'dar an sooy']}]})


@app.route('/api/people/path/<int:person_id>', methods=['GET'])
def find_path(person_id):
    return jsonify(path=[{'actor': 'sean penn', 'movie': 'mystic'}, {'name': 'clint', 'movie': 'movie2'}])

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
