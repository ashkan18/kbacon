__author__ = 'Ashkan'


class ModelTypes(object):
    ARTIST = 1
    MOVIE = 2


def jsonify_artist_model(artist_model):
    artist_json = {'name': artist_model.info['name']}
    if 'image' in artist_model.info:
        artist_json['image'] = artist_model.info['image']
    else:
        artist_model.info['image'] = ''
    artist_json['type'] = ModelTypes.ARTIST
    return artist_json


def jsonify_movie_model(movie_model):
    return {'name': movie_model.info['name'], 'image': movie_model.info['image'], 'type': ModelTypes.MOVIE}