window.Artist = Backbone.Model.extend({
    /**
     * This is the backbone model to get an artist
     */
    urlRoot:"../api/artists/",

    initialize:function () {
        this.list = new ArtistCollection();
        this.list.url = '../api/artists/' + this.id + '/path';
    }

});

window.ArtistCollection = Backbone.Collection.extend({
    /**
     * This is the collection for getting list of artists,
     * it handles call to search for artists
     */
    model: Artist,

    url:"../api/artist",

    findByName:function (key) {
        // generate the url to call for searching users
        var url = (key == '') ? '../api/artists' : "../api/artists/search/?query=" + key;
        console.log('findByName: ' + key);
        var self = this; // bind the model
        $.ajax({
            url:url,
            dataType:"json",
            success:function (data) {
                // reset the model and pass the artists from json result we got back for search
                self.reset(data['artists']);
            }
        });
    }

});