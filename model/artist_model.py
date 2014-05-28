

__author__ = 'Ashkan'


class ArtistModel(object):

    def __init__(self, artist_id, artist_data):
        self.id = artist_id
        self.info = artist_data
        self.films = []
