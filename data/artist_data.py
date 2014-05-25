from os import listdir
import os
from os.path import join, isfile
import json
import uuid
from flask import current_app
from model.artist_model import ArtistModel
from model.movie_model import MovieModel

__author__ = 'Ashkan'

artist_dict = {}
film_dict = {}


FILMS_FOLDER_PATH = os.path.join(os.path.dirname(__file__), '../films/')


class ArtistData(object):

    def init_data(self):
        for f in listdir(FILMS_FOLDER_PATH):
            file_full_path = join(FILMS_FOLDER_PATH, f)
            if isfile(file_full_path):
                self.__read_file(file_full_path)

    def __read_file(self, json_file):
        with open(json_file) as json_file:
            json_data = json.load(json_file)
            if 'film' in json_data:
                # generate a guid since we can't use names,
                # names cause issues when we have same name few times
                # ex. Last Holiday we have it two times and we can't use them as key
                film_uuid = uuid.uuid1()

                # create new movie model by json data
                movie_model = MovieModel(film_uuid, json_data)
                film_dict[film_uuid] = movie_model

                # now parse the cast data of the film to generate artist dict
                if 'cast' in json_data and len(json_data['cast']) > 0:
                    for cast in json_data['cast']:
                        # create a new artist model from the cast info
                        artist_model = ArtistModel(cast)

                        if artist_model.info['name'] not in artist_dict:
                            # first time seeing this artist,
                            # we haven't had this artist in the dict yet
                            # add them to the dict
                            artist_model.films.append(film_uuid)
                            artist_dict[artist_model.info['name']] = artist_model
                        else:
                            # we already had this artist before
                            # no need to update the info, just add the film
                            artist_dict[artist_model.info['name']].films.append(film_uuid)
                else:
                    print(u"Movie {0} had no cast".format(movie_model.info['name']))
            else:
                print(u"Missing film in json: {0}".format(json_data))

    def artist_exist(self, artist_name):
        return artist_name in artist_dict

    def get_all_films_for_artist(self, artist_name):
        current_app.logger.info(u'1---->{0}'.format(artist_name))
        current_app.logger.info(u'2-------->{0}'.format(artist_dict[artist_name]))
        current_app.logger.info(u'3---------->{0}'.format(artist_dict[artist_name].films))
        for film in artist_dict[artist_name].films:
            yield film

    def get_movie_by_id(self, movie_id):
        if movie_id in film_dict:
            return film_dict[movie_id]
        else:
            return None

    def get_actor_by_name(self, actor_name):
        if actor_name in artist_dict:
            return artist_dict[actor_name]
        else:
            return None

    def search_artists_by_name(self, name):
        return list(artist_model for artist_name, artist_model in artist_dict.iteritems()
                    if name.lower() in artist_name.lower())
