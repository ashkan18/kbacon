/**
 * This file defines HeaderView which basically shows the header bar with search input
 * and handles showing the result of the search for artists
 */
window.HeaderView = Backbone.View.extend({
    el: '#header',

    initialize: function () {
        // define search result and the view for showing the results
        this.searchResults = new ArtistCollection();
        this.searchresultsView = new ArtistListView({model: this.searchResults});

        // render the header section in init
        this.render();
    },

    render: function () {
        $(this.el).html(this.template());
        $('.navbar-search', this.el).append(this.searchresultsView.render().el);
        return this;
    },

    events: {
        "keyup .search-query": "search",
        "keypress .search-query": "onkeypress"
    },

    search: function () {
        var key = $('#searchText').val();
        console.log('search ' + key);
        this.searchResults.findByName(key);
        setTimeout(function () {
            $('.dropdown').addClass('open');
        });
    },

    onkeypress: function (event) {
        // remove the default action of enter key for this search box
        if (event.keyCode == 13) {
            event.preventDefault();
        }
    },

    select: function(menuItem) {
        $('.nav li').removeClass('active');
        $('.' + menuItem).addClass('active');
    }

});