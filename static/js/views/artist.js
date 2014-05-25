window.ArtistView = Backbone.View.extend({

    tagName:"div",
    initialize:function () {
    },

    render: function () {

        //$(this.el).html(this.template(this.model.toJSON()));
        var path = this.model.toJSON()['path'];
        console.log("===>"+ path);
        _.each(path, function (path_item) {
            console.log("----->" + JSON.stringify(path_item));
            $(this.el).append(this.template(path_item));
        }, this);

        return this;
    }
});

