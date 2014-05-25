__author__ = 'root'


class ModelTypes(object):
    ARTIST = 1
    MOVIE = 2


def jsonify_artist_model(actor_model):
    artist_json = {'name': actor_model.info['name']}
    if 'image' in actor_model.info:
        artist_json['image'] = actor_model.info['image']
    else:
        actor_model.info['image'] = ''
    artist_json['type'] = ModelTypes.ARTIST
    return artist_json


def jsonify_movie_model(movie_model):
    return {'name': movie_model.info['name'], 'image': movie_model.info['image'], 'type': ModelTypes.MOVIE}