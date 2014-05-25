import json

__author__ = 'Ashkan'


class ArtistModel(object):

    def __init__(self, artist_data):
        self.info = artist_data
        self.films = []

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)

        import simplejson
        return simplejson.dumps(d)

    def to_JSON(self):
        print 'hello'

