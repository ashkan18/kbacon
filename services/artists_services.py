"""
This module defines all the methods needed for getting artists and their related information

"""

from data.artist_data import ArtistData
from helpers.json_helper import jsonify_artist_model, jsonify_movie_model
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


def get_all_artists():
    pass


def find_path_between_artists(artist_name):
    """
    This method finds the path between artists. a path is a combination of artists and films that connects this artist
    with Kevin Bacon

    @param artist_name: name of the artist we want to find his/her path to Kevin Bacon
    @return: list of jsonified artist and films model
    """
    path = shortest_link(artist_name)

    # now that we have the path now create a list of artist and models models
    # each item in path is a tuple of (artist, film)
    final_path = []
    for path_item in path:
        actor_name = path_item[0]
        movie_id = path_item[1]
        actor_model = __artist_data.get_artist_by_name(actor_name)
        movie = __artist_data.get_movie_by_id(movie_id)

        if movie is not None:
            # first item in the tuple is always without movie since it's the starting artist
            final_path.append(jsonify_movie_model(movie))
        final_path.append(jsonify_artist_model(actor_model))

    current_app.logger.info(u'The path from {0} to KB has {1} items'.format(artist_name, len(path)))
    return final_path


def shortest_link(actor_name):
    """Return a list of actors (actors are strings)that represents the shortest
    connection between 'actor_name' and Kevin Bacon that can be found in the
    dictionaries: 'actor_dict' and 'movie_dict'.
    """

    # Note about the algorithm:
    # Type: Breadth first
    # First, check if the actor's name is 'Kevin Bacon' or if the actor is
    # not present in the 'actor_dict'. If either of them if True
    # then return the empty list.
    if actor_name.lower() == 'kevin bacon' or not __artist_data.artist_exist(actor_name):
        return []

    # get the actor from our list
    investigated = [actor_name]
    to_investigate = [[(actor_name, '')]]

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
        actor_name = actor_link[len(actor_link) - 1][0]
        for movie_id in __artist_data.get_all_films_for_artist(actor_name):
            movie = __artist_data.get_movie_by_id(movie_id)
            for co_star in movie.casts:

                # if we haven't checked this co-star yet
                if not (co_star in investigated):
                    co_star_name = co_star['name']
                    if co_star_name == "Kevin Bacon":
                        # Kevin Bacon was in the list, yesss we found him!!
                        actor_link.append(("Kevin Bacon", movie.id))
                        return actor_link

                    # If the co_star is not present in the list of
                    # investigated actors then make a list containing
                    # the entire link from 'actor_name' to the co_star
                    # and add it to the nested list 'to_investigate'.
                    elif not (co_star_name in investigated):
                        investigated.append(co_star_name)
                        full_link = actor_link[:]
                        full_link.append((co_star_name, movie.id))
                        to_investigate.append(full_link)

        # Remove the actor_link from the to_investigate since we just investigated this artist
        # getting here means this artist didn't help in finding Kevin Bacon
        to_investigate.remove(actor_link)
    return []
