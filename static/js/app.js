window.Router = Backbone.Router.extend({

    routes: {
        "": "home",
        "artist/:id": "artistDetails"
    },

    initialize: function () {
        // show header section on the initiliaze of the app
        this.headerView = new HeaderView();

        // Close the search dropdown on click anywhere in the UI
        $('body').click(function () {
            $('.dropdown').removeClass("open");
        });
    },

    // showing the landing page content
    home: function () {
        // render home page by creating home view
        this.homeView = new HomeView();
    },

    artistDetails: function(id)  {
        // first clear the content area
        $('#pleaseWaitDialog').modal({show:true});
        var artist = new Artist({id: id});
        // get artist details (including path) from the server
        artist.fetch({
            success: function (data) {
                $('#pleaseWaitDialog').modal('hide');
                console.log("Artist detail:" + JSON.stringify(data));
                $('#content').html(new ArtistView({model: data}).render().el);
            }
        });
    }
});


// this is defined in templateLoader.js
templateLoader.load(["HomeView", "HeaderView", 'ArtistListItemView', 'ArtistView'],
    function () {
        // after loading templates now start the app
        app = new Router();
        Backbone.history.start();
    });