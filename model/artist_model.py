

__author__ = 'Ashkan'


class ArtistModel(object):
    """
    This class defines an artist model, an artist has an id, info which is a dict and list of films
    """
    def __init__(self, artist_id, artist_data):
        self.id = artist_id
        self.info = artist_data
        self.films = []
