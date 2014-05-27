window.ArtistView = Backbone.View.extend({
    className: 'row',

    initialize:function () {
    },

    render: function () {
        // response coming back from the server has a path which shows the path from
        // requested artist to Kevin Bacon
        var path = this.model.toJSON()['path'];
        // each item in the path, except the first one, has an artist and a movie
        // sample, Sean Penn, mystic river, Kavin Bacon
        // because of the fact that first item doesn't have a movie we have to decrease the path by 1
        // and then divide it by two to get the actual distance
        var distance = (path.length - 1) / 2;
        console.log("path received for this artist"+ path);
        $(this.el).append(this.template({'distance': distance, 'path':path, 'id': this.model.toJSON()['id']}));

        return this;
    }
});




