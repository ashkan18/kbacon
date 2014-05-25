window.Artist = Backbone.Model.extend({

    urlRoot:"../api/artists/",

    initialize:function () {
        this.list = new ArtistCollection();
        this.list.url = '../api/artists/' + this.id + '/path';
    }

});

window.ArtistCollection = Backbone.Collection.extend({

    model: Artist,

    url:"../api/artist",

    findByName:function (key) {
        var url = (key == '') ? '../api/artists' : "../api/artists/search/?query=" + key;
        console.log('findByName: ' + key);
        var self = this;
        $.ajax({
            url:url,
            dataType:"json",
            success:function (data) {
                console.log("---->" + data['artists'].length);
                console.log("search success: " + JSON.stringify(data['artists']));
                self.reset(data['artists']);
            }
        });
    }

});