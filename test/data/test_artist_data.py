# coding=utf-8
import unittest
from artist_data import ArtistData
from test.logger import logger

__author__ = 'Ashkan'


class AppHelpersSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("Firing up serialize helpers unit test suite ...")

    def test_get_cast_id_for_name(self):
        """
            Test artist_data.get_cast_id_for_name to make sure it always generates correct id and handle utf8
        """
        artist_data = ArtistData()

        artist_name = u'Alejandro González Iñárritu'

        artist_id = artist_data.get_cast_id_for_name(artist_name)

        # make sure it successfully
        self.assertIsNotNone(artist_id, 'make sure it can successfully get id for utf8')

        # make sure second time we call this method returns the same id
        self.assertEqual(artist_id, artist_data.get_cast_id_for_name(artist_name),
                         'make sure it gives same id back second time')

        # make sure it's not case sensitive
        self.assertEqual(artist_id, artist_data.get_cast_id_for_name(artist_name.lower()),
                         "make sure it's not case sensitive")

        # make sure it takes care of spaces
        artist_name_with_space = u"Alejandro    González    Iñárritu"
        self.assertNotEqual(artist_id, artist_data.get_cast_id_for_name(artist_name_with_space),
                            "make sure it takes care of spaces")
