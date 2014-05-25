__author__ = 'Ashkan'


class MovieModel(object):

    def __init__(self, id, movie_data):
        self.id = id
        self.info = movie_data['film']
        self.casts = movie_data['cast']

