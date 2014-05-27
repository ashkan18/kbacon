window.ArtistView = Backbone.View.extend({
    className: 'row',

    initialize:function () {
    },

    render: function () {
        // response coming back from the server has a path which shows the path from
        // requested artist to Kevin Bacon
        var path = this.model.toJSON()['path'];
        var distance = path.length;
        console.log("path received for this artist"+ path);
        $(this.el).append(this.template({'distance': distance, 'path':path}));

        return this;
    }
});




