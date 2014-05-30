window.Artist = Backbone.Model.extend({
    /**
     * This is the backbone model to get an artist
     */
    urlRoot:"../api/artists/",

    initialize:function () {
        this.list = new ArtistSearchCollection();
    }

});


window.ArtistSearchCollection = Backbone.Collection.extend({
    /**
     * This is the collection for getting list of artists,
     * it handles call to search for artists
     */
    model: Artist,

    url:"../api/artists/search",

    parse: function( dataResponse ) {
        // we need to send artists back from the response we got
        this.sort();
        return dataResponse.artists;
    },

    comparator: function(artistModel) {
        return artistModel.get('name');
    }

});


