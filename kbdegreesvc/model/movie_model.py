__author__ = 'Ashkan'


class MovieModel(object):
    """
    This class defines a Movie model, a movie model has an id, info which is a dict of info and list of casts
    """
    def __init__(self, id, movie_data):
        """
        This constructor gets a json data read from source that has movie info and sets proper attributes
        of this model
        @param id: unique id representing this movie
        @param movie_data: json data related to this movie
        """
        self.id = id
        self.info = movie_data['film']
        self.casts = movie_data['cast']

