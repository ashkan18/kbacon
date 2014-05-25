window.ArtistView = Backbone.View.extend({

    className: 'row',  // this element should be in a row

    initialize:function () {
    },

    render: function () {
        // response coming back from the server has a path which shows the path from
        // requested artist to Kevin Bacon
        var path = this.model.toJSON()['path'];
        console.log("path received for this artist"+ path);
        _.each(path, function (path_item) {
            $(this.el).append(this.template(path_item));
        }, this);

        return this;
    }
});

