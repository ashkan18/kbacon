window.Router = Backbone.Router.extend({

    routes: {
        "": "home",
        "artist/:id": "artistDetails"
    },

    initialize: function () {
        this.headerView = new HeaderView();
        $('.header').html(this.headerView.render().el);

        // Close the search dropdown on click anywhere in the UI
        $('body').click(function () {
            $('.dropdown').removeClass("open");
        });
    },
    home: function () {
        // Since the home view never changes, we instantiate it and render it only once
        if (!this.homeView) {
            this.homeView = new HomeView();
            this.homeView.render();
        }

        $("#content").html(this.homeView.el);
        this.headerView.select('home-menu');
    },

    artistDetails: function(id)  {
        var artist = new Artist({id: id});
        artist.fetch({
            success: function (data) {
                // Note that we could also 'recycle' the same instance of EmployeeFullView
                // instead of creating new instances
                $('#content').html(new ArtistView({model: data}).render().el);
            }
        });

    }
});



// this is defined in templateLoader.js
templateLoader.load(["HomeView", "HeaderView"],
    function () {
        // after loading templates now start the app
        app = new Router();
        Backbone.history.start();
    });