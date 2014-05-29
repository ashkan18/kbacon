"""
This module defines all the methods needed for getting artists and their related information

"""

from kbdegreesvc.data.artist_data import ArtistData
from kbdegreesvc.helpers.json_helper import jsonify_artist_model, jsonify_movie_model
from flask import current_app

__author__ = 'Ashkan'

__artist_data = ArtistData()
__artist_data.init_data()


def search_artists(search_query):
    """
    Passed a search query this method returns the list of artist matching this search term
    @param search_query: String term we are looking for artist with this string.
    @return: list of artist models with this search term in their name
    """
    return __artist_data.search_artists_by_name(search_query)


def get_artist_by_id(artist_id):
    """
    This method returns an ArtistModel for this artist_id
    @param artist_id: String id of the artist we are looking for
    @return: ArtistModel of this artist_id
    """
    return __artist_data.get_artist_by_id(artist_id)


def find_path_between_artists(artist_id):
    """
    This method finds the path between artists. a path is a combination of artists and films that connects this artist
    with Kevin Bacon

    @param artist_id: unique id of the artist we want to find his/her path to Kevin Bacon
    @return: list of jsonified artist and films model
    """
    path = shortest_link(artist_id)

    # now that we have the path now create a list of artist and models models
    # each item in path is a tuple of (artist, film) exampl;
    # [(u'57e379d456c58ed96b6673eab7730308dc08c582', ''),
    #  ('e3a27d5c32004005c1d0fb39172c2a02f3c7f1c4', UUID('78d7761c-e741-11e3-a1d1-000c2953ae0f'))]
    final_path = []
    for path_item in path:
        actor_id = path_item[0]
        movie_id = path_item[1]
        actor_model = __artist_data.get_artist_by_id(actor_id)
        movie = __artist_data.get_movie_by_id(movie_id)

        if movie is not None:
            # first item in the tuple is always without movie since it's the starting artist
            final_path.append(jsonify_movie_model(movie))
        final_path.append(jsonify_artist_model(actor_model))

    current_app.logger.info(u'The path from {0} to KB has {1} items'.format(artist_id, len(path)))
    return final_path


def shortest_link(actor_id):
    """Return a list of actors (actors are strings)that represents the shortest
    connection between 'actor_name' and Kevin Bacon that can be found in the
    dictionaries: 'actor_dict' and 'movie_dict'.
    """

    # Note about the algorithm:
    # Type: Breadth first
    # First, check if the actor's name is 'Kevin Bacon' or if the actor is
    # not present in the 'actor_dict'. If either of them if True
    # then return the empty list.
    kevin_bacon_artist_id = __artist_data.get_cast_id_for_name('kevin bacon')
    if actor_id == kevin_bacon_artist_id or not __artist_data.artist_exist(actor_id):
        return []

    # get the actor from our list
    investigated = [actor_id]
    to_investigate = [[(actor_id, '')]]

    # The loop condition checks if the list to_investigate has any remaining
    # elements.
    while to_investigate:
        # Note: As the distance increases the size of each sublist in
        # the nested list 'to_investigate' increases proportionally.
        # The last actor of each sublist is the actor to be investigated
        # The actors which occur before the actor in the sublist simply
        # represent the link from 'actor_name' to that actor.
        # Loop property: The zeroth index changes on every iteration.
        actor_link = to_investigate[0]

        # get the actor name from the actor link
        # actor link is a list of tuple, example:
        # [(actor_model, movie_model), (actor_model2, movie_model2)]
        actor_id = actor_link[len(actor_link) - 1][0]
        for movie_id in __artist_data.get_all_films_for_artist(actor_id):
            movie = __artist_data.get_movie_by_id(movie_id)
            for co_star in movie.casts:
                co_star_name = co_star['name']
                co_star_id = __artist_data.get_cast_id_for_name(co_star_name)
                # if we haven't checked this co-star yet
                if not (co_star in investigated):
                    if co_star_name == "Kevin Bacon":
                        # Kevin Bacon was in the list, yesss we found him!!
                        actor_link.append((kevin_bacon_artist_id, movie.id))
                        return actor_link

                    # If the co_star is not present in the list of
                    # investigated actors then make a list containing
                    # the entire link from 'actor_name' to the co_star
                    # and add it to the nested list 'to_investigate'.
                    elif not (co_star_id in investigated):
                        investigated.append(co_star_id)
                        full_link = actor_link[:]
                        full_link.append((co_star_id, movie.id))
                        to_investigate.append(full_link)

        # Remove the actor_link from the to_investigate since we just investigated this artist
        # getting here means this artist didn't help in finding Kevin Bacon
        to_investigate.remove(actor_link)
    return []


def get_all_artists():
    #TODO: implement this when it's needed
    pass


