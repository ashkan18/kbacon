from flask import Flask
import artists_services
from helpers.json_helper import ModelTypes

__author__ = 'Ashkan'
from test.logger import logger
from flask.ext.testing import TestCase

SEAN_PENN_ARTIST_ID = '57e379d456c58ed96b6673eab7730308dc08c582'
KEVIN_BACON_ARTIST_ID = 'e3a27d5c32004005c1d0fb39172c2a02f3c7f1c4'


class ArtistServiceSuite(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_find_path_between_artists(self):
        """
            Test Find Path Between Artists
        """
        path = artists_services.find_path_between_artists(SEAN_PENN_ARTIST_ID)

        # make sure we have 3 items in the path from sean penn  to kevin bacon, sean penn, mystic river, kevin bacon
        self.assertEqual(len(path), 3, "Test Sean Penn's separation degree")

        # make sure first item is sean penn
        sean_penn_item_path = path[0]
        self.assertEqual(sean_penn_item_path['name'], 'Sean Penn')
        self.assertNotEqual(sean_penn_item_path['image'], '', 'make sure image is not empty')
        self.assertEqual(sean_penn_item_path['type'], ModelTypes.ARTIST)

        # make sure second item is Mystic River
        mystic_river_item = path[1]
        self.assertEqual(mystic_river_item['name'], 'Mystic River', 'Make sure the name is as expected')
        self.assertNotEqual(mystic_river_item['image'], '', 'Make sure we have image for the film')
        self.assertEqual(mystic_river_item['type'], ModelTypes.MOVIE)

        # make sure third item is kevin bacon
        kb_item_path = path[2]
        self.assertEqual(kb_item_path['name'], 'Kevin Bacon')
        self.assertNotEqual(kb_item_path['image'], '', 'make sure image is not empty')
        self.assertEqual(kb_item_path['type'], ModelTypes.ARTIST)

    def test_shortest_link_success(self):
        """
            Test successful shortest path link for sean penn
        """
        path = artists_services.shortest_link(SEAN_PENN_ARTIST_ID)

        # expected path
        #  [(u'57e379d456c58ed96b6673eab7730308dc08c582', ''),
        # ('e3a27d5c32004005c1d0fb39172c2a02f3c7f1c4', UUID('78d7761c-e741-11e3-a1d1-000c2953ae0f'))]
        # note uuid here is generated each time so we can't check for this exact number
        # make sure each item is what we expect
        # first item should be a tuple, where first item is sean penn and second one (film) is empty
        sean_penn_item_tuple = path[0]
        self.assertEqual(sean_penn_item_tuple[0], SEAN_PENN_ARTIST_ID, "Test first item is Sean Penn")
        self.assertEqual(sean_penn_item_tuple[1], '', "Make sure second item in tuple is empty")

        kevin_bacon_item_tuple = path[1]
        self.assertEqual(kevin_bacon_item_tuple[0], KEVIN_BACON_ARTIST_ID, 'Make sure we have KB')
        self.assertIsNotNone(kevin_bacon_item_tuple[1], "Make sure we know the film connecting to KB")

    def test_shortest_link_fail_fake_id(self):
        """
            Test path for fake artist id
        """
        fake_artist_id = 'ashkannasseri'
        path = artists_services.shortest_link(fake_artist_id)
        self.assertEqual(len(path), 0, "Test path is empty for non-exsting artist id")

    def test_shortest_link_for_kevin_bacon(self):
        """
            Test shortest path for kevin bacon
        """
        path = artists_services.shortest_link(KEVIN_BACON_ARTIST_ID)
        self.assertEqual(len(path), 0, "Test path is empty for kevin bacon!")


