/**
 * This file defines HeaderView which basically shows the header bar with search input
 * and handles showing the result of the search for artists
 */
window.HeaderView = Backbone.View.extend({
    el: '#header',

    SEARCH_FIELD_SELECTOR: "#searchText",
    SEARCH_DELAY: 500,
    MINIMUM_SEARCH_LENGTH: 2,

    initialize: function () {
        // define search result and the view for showing the results
        this.searchResults = new ArtistSearchCollection();
        this.searchresultsView = new ArtistListView({model: this.searchResults});

        // will be used to manage the auto-search feature
        this.searchTimeout = null;
        // render the header section in init
        this.render();
    },

    render: function () {
        $(this.el).html(this.template());
        $('.navbar-search', this.el).append(this.searchresultsView.render().el);
        return this;
    },

    events: {
        // we want to search each time user adds a character to search input
        "keyup .search-query": "checkToSearch",
        "keypress .search-query": "onkeypress"
    },

    checkToSearch: function( e ) {
        // only call search if we have passed the delay, if it's before that clear timeout and ask a new one
        if ( this.searchTimeout ) {
            clearTimeout( this.searchTimeout );
        }

        // create a new settimeout which means run the search after SEARCH_DELAY
        this.searchTimeout = setTimeout(function() {
            this.search(this.$( this.SEARCH_FIELD_SELECTOR ).val());
        }.bind( this ), this.SEARCH_DELAY );
    },


    search: function ( searchTerm ) {
        // when user inputs in search text input, we check if search text is > 3 characters
        // we search the server, the reason is we get lot of results for less than 3 characters
        if (searchTerm.length > this.MINIMUM_SEARCH_LENGTH) {
            //this.searchResults.findByName(searchTerm);
            this.searchResults.fetch({
                type: 'GET',
                data: {'query': searchTerm}
            });
            setTimeout(function () {
                $('.dropdown').addClass('open');
            });
        } else {
            this.searchresultsView.clearResults();
        }
    },

    onkeypress: function (event) {
        // remove the default action of enter key for this search box
        if (event.keyCode == 13) {
            event.preventDefault();
        }
    },

    select: function(menuItem) {
        // show items as selected when mouse over
        $('.nav li').removeClass('active');
        $('.' + menuItem).addClass('active');
    }

});