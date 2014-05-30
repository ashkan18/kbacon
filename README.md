Six Degree of Bacon
==================
This app is used to find the Kevin Bacon degree for other artists.

What is Kevin Bacon Degree?
==================
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
================
This app is written in Python(Flask), Bootstrap and Backbone. For testing on the back-end I've used Flask-Testing and
nosetest for getting the code coverage of the tests.

Back-end Design
---------
Backend is all based on python flask micro-framework. You can find the back-end code under kbdegreesvc folder. The code starts from kbdegree.py file. In this file we create a
new flask application and define all the endpoints. We have two important endpoints there
- search_artist: gets a 'query' as get request parameter and returns a list of artist with the query in their name
- find_path: gets artist id in the path and based on that returns a path from that artist id to Kevin Bacon

Endpoints (interfaces) job is to validate the request and present the response of each request to the users, to handle
the core logic, they make call to service layer.

**artists_services.py:** Service layer is the place for storing the core logic of this app. Currently we have artist_service
there which is used to define all the functionality we support for accessing artist data. This layer should not directly
access the data, the reason behind this decision is, this way we encapsulate the data access layer and in the future
we can easily switch from one data access layer to another without touching the service layer. In a nutshell,
service layer doesn't care how and from where we get the data.

**data/artist_data.py:** Service layer uses data layer to access the data. artist_data holds the logic for initializing
and accessing the data for
artists and movies.

**model/artist_model.py:**: Class defining an artist in our app
**model/movie_model.py:**: Class defining a movie in our app

I also have helper method json_helper.py which takes care of creating json result for artist and movie models.

**Backend Testing**: I have used Flask-Testing and python unittest modules for handling test cases. You can find python unit test files under:
/test/data and test/services
under each folder you can run:

    nosetests -v --with-coverage --cover-package=data --logging-level=CRITICAL
    nosetests -v --with-coverage --cover-package=services --logging-level=CRITICAL

These will run unittest and also give the current code coverage of the tests. Current code coverage on first suite is 83% and on second suite is 94%

Front-end Design
-----------
On the front-end, I used bootstrap to get the proper layout and css classes, and used backbone for handling client side
logic, calling to server and render the ui. I've also used Grunt to concat and minify the javascript code, after running grunt all the javascript files and their dependencies will end up in one KBDegree.min.js file under static/js.

We have an index.html which basically imports one KBDegree.min.js script. You can see the actual different sources of this script under src/ folder. Here is a little more details about files under src:

app.js is where my backbone router is defined. In this file I define two routes that I have in my app:
- '': which goes to the home page. This route create a new HomeView. HomeView will render the HomeView.html underscore
based template and will put the result in a div with 'content' as it's id.

- 'artist/:id': This route will fetch an artist from the server using Artist model. Then passes the result of fetching
artist details to ArtistView which will render the artist path to Kevin Bacon and update the #content div.

HeaderView is the view that handles rendering the header area, it creates a new SearchListView and passes the id of
the search text input element, this way SearchListView is more modular and can be used by any other view.

SearchListView is responsible for the functionality of the instant search. On the keyup of the keyboard
on the search box, it will wait 1 second if the user has not added any more characters it will make a call to server to
get a list of artists with this input text in their name and shows the results as a dropdown under the search text box.

SearchListView uses ArtistSearchCollection for calling the server and getting list of artists.

**templateLoader.js**: This file has a method that handles loading the template html files from tpl folder (by making
ajax get calls) and read the html and sets them for their proper view. This way we can have a separate folder containing
the templates.

**Frontend Unittest**: THIS IS A WORK IN PROGRESS, but for now I have set up Jasmine and sinos for testing my backbone based application. You can find a sample of a test under /test/js. The main problem with setting up the test right now is the fact that I'm rendering templates from files and Jasmine has issues getting the files. This issue will be fixed once I use grunt to pre-generate the templates. You can run the test by opening test/js/specRunner.html

Improvements to make
===========
- Use datastore instead of in-memory dict: right now I'm using in memory dict for storing artist and movies. this
possibly means using lot of memory of the server, In next phase I will switch to use NOSQL datastores for this.

- Use d3 for showing a graph: Right now I'm only using images to show the relation between artists and movies,
it would be cool if I use d3 to show visually better relations.

- Use grunt to pre-generate underscore templates

- Add favicon: Missing it now


Run the app locally
===========
You can run the app locally by running

    python kbdegree.py

This will run the server on port 5000 and you can access the main page on:
http://localhost:5000/static/index.html

