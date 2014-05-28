__author__ = 'Ashkan'


class ModelTypes(object):
    """
    This class defines consts for Artist and Movie models,
    I don't have these in the model itself since its mostly a presentation thing and didn't want to
    have models dealing with presentation
    """
    ARTIST = 1
    MOVIE = 2


def jsonify_artist_model(artist_model):
    """
    This method gets an artist model and creates proper json object
    @param artist_model: ArtistModel object we want to get it's json representation
    @return: json representation of this ArtistModel
    """
    artist_json = {'name': artist_model.info['name']}
    if 'image' in artist_model.info:
        artist_json['image'] = artist_model.info['image']
    else:
        # set image to empty string, UI should handle showing proper default image
        artist_model.info['image'] = ''
    artist_json['type'] = ModelTypes.ARTIST
    artist_json['id'] = artist_model.id
    return artist_json


def jsonify_movie_model(movie_model):
    """
    This method generates a proper json response for a MovieModel
    @param movie_model: MovieModel we want to get it's json representation
    @return: json representation of this MovieModel
    """
    return {'name': movie_model.info['name'], 'image': movie_model.info['image'], 'type': ModelTypes.MOVIE}