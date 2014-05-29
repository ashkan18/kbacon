# coding=utf-8
import unittest
from artist_data import ArtistData
from test.logger import logger

__author__ = 'Ashkan'


class ArtistDataSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("Firing up artist_data unit test suite ...")

    def setUp(self):
        self.artist_data = ArtistData()
        self.artist_data._ArtistData__clear_data()
        self.artist_data._ArtistData__read_file('forrestgump.json')

    def test_get_cast_id_for_name(self):
        """
            Test artist_data.get_cast_id_for_name to make sure it always generates correct id and handle utf8
        """

        artist_name = u'Alejandro González Iñárritu'

        artist_id = self.artist_data.get_cast_id_for_name(artist_name)

        # make sure it successfully
        self.assertIsNotNone(artist_id, 'make sure it can successfully get id for utf8')

        # make sure second time we call this method returns the same id
        self.assertEqual(artist_id, self.artist_data.get_cast_id_for_name(artist_name),
                         'make sure it gives same id back second time')

        # make sure it's not case sensitive
        self.assertEqual(artist_id, self.artist_data.get_cast_id_for_name(artist_name.lower()),
                         "make sure it's not case sensitive")

        # make sure it takes care of spaces
        artist_name_with_space = u"Alejandro    González    Iñárritu"
        self.assertNotEqual(artist_id, self.artist_data.get_cast_id_for_name(artist_name_with_space),
                            "make sure it takes care of spaces")

    def test_read_file(self):
        """
            Test reading json file and make sure we create proper dicts
        """
        tom_hanks_artist_id = self.artist_data.get_cast_id_for_name("Tom Hanks")

        tom_hanks_artist_model = self.artist_data.get_artist_by_id(tom_hanks_artist_id)

        # make sure we have him in our data
        self.assertIsNotNone(tom_hanks_artist_model, "make sure we have him in our data")
        self.assertEqual(tom_hanks_artist_model.info['name'], "Tom Hanks")

        # make sure he has only one movie in his list of movies
        self.assertEqual(len(tom_hanks_artist_model.films), 1, "make sure he has only one movie in his list of movies")

        forrest_gump_id = tom_hanks_artist_model.films[0]

        forrest_gump_model = self.artist_data.get_movie_by_id(forrest_gump_id)

        # make sure we have the movie in our data
        self.assertIsNotNone(forrest_gump_model, "make sure we have the movie in our data")

        # make sure movie name and image is correct
        self.assertEqual(forrest_gump_model.info['name'], "Forrest Gump", "make sure movie name is correct")
        self.assertEqual(forrest_gump_model.info['image'],
                         "http://image.tmdb.org/t/p/w185/z4ROnCrL77ZMzT0MsNXY5j25wS2.jpg",
                         "make sure movie image is correct")

        # make sure it has expected number of casts
        self.assertEqual(len(forrest_gump_model.casts), 9, "make sure it has expected number of casts")

    def test_search_results(self):
        """
            Test search functionality
        """
        search_results = self.artist_data.search_artists_by_name("Tom Hanks")
        self.assertEqual(len(search_results), 1)

        # make sure search is not case sensative
        search_results = self.artist_data.search_artists_by_name("tom hanks")
        self.assertEqual(len(search_results), 1)

        # search for 'll' should return 4
        search_results = self.artist_data.search_artists_by_name("ll")
        self.assertEqual(len(search_results), 4)

    def test_artist_exist(self):
        """
            Test artists exist
        """
        tom_hanks_artist_id = self.artist_data.get_cast_id_for_name("Tom Hanks")

        self.assertTrue(self.artist_data.artist_exist(tom_hanks_artist_id), "make sure tom hanks exist")

        # make sure garbage does not exist!
        self.assertFalse(self.artist_data.artist_exist("garbage"), "make sure tom hanks exist")





