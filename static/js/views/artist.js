window.ArtistView = Backbone.View.extend({

    tagName:"div",
    initialize:function () {
    },

    render: function () {
        $(this.el).html(this.template(this.model.toJSON()));

        return this;
    }
});

