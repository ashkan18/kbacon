window.ArtistView = Backbone.View.extend({
    className: 'row',

    initialize:function () {
    },

    render: function () {
        // response coming back from the server has a path which shows the path from
        // requested artist to Kevin Bacon
        var path = this.model.toJSON()['path'];
        if (path.length === 0) {
            // there was no path, it's either we are searching for Kevin Bacon himself
            // or there was no path from this artist to Kevin Bacon (infinite distance)
            var message = '';
            if (this.model.toJSON()['artist_name'] === 'Kevin Bacon'){
                message = 'Are you kidding me?! Kevin Bacon knows himself!';
            } else {
                message = 'Hmmmm..... Looks like this artist is pretty far from KB!';
            }
            $(this.el).append("<h2 class='text-center'>" + message + "</h2>");
        } else {
            // each item in the path, except the first one, has an artist and a movie
            // sample, Sean Penn, mystic river, Kavin Bacon
            // because of the fact that first item doesn't have a movie we have to decrease the path by 1
            // and then divide it by two to get the actual distance
            var distance = (path.length - 1) / 2;
            $(this.el).append(this.template({'distance': distance, 'path':path, 'name': this.model.toJSON()['artist_name']}));
        }
        return this;
    }
});




