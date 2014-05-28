Six Degree of Bacon
======================

This app is used to find the Kevin Bacon degree for other artists.

What is Kevin Bacon Degree?
========
Six Degrees of Kevin Bacon is a parlor game based on the "six degrees of separation" concept,
which posits that any two people on Earth are six or fewer acquaintance links apart.
That idea eventually morphed into this parlor game, wherein movie buffs challenge each other
to find the shortest path between an arbitrary actor and prolific Hollywood
character actor Kevin Bacon. It rests on the assumption that any individual involved in the Hollywood,
California, film industry can be linked through his or her film roles to Kevin Bacon within six steps.
The game requires a group of players to try to connect any such individual to Kevin Bacon as quickly
as possible and in as few links as possible. It can also be described as a trivia game based on
the concept of the small world phenomenon. In 2007, Bacon started
a charitable organization named <a href="http://SixDegrees.org">SixDegrees.org


About The Code
=========
This app is written in Python(Flask), Bootstrap and Backbone.

On the back-end, we have three layers.
    . Interface layer: Where we define the routes and endpoints</li>
    . Services layer: Where we have the core logic for example finding the path from each artist to Kevin Bacon
    . Data layer: Which handles storing and fetching the data from the data structure.

On the front-end, I used bootstrap to get the proper layout and css classes, and used backbone for handling client side
logic, calling to server and render the ui.


Improvements to make
===========
- Use datastore instead of in-memory dict: right now I'm using in memory dict for storing artist and movies. this
possibly means using lot of memory of the server, In next phase I will switch to use NOSQL datastores for this.

- Use d3 for showing a graph: Right now I'm only using images to show the relation between artists and movies,
it would be cool if I use d3 to show visually better relations.

- Add fav.ico: Missing it now
