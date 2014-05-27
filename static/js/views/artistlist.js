/**
 * This view handles showin list of artists
 *
 */
window.ArtistListView = Backbone.View.extend({

    tagName:'ul',

    className: 'dropdown-menu',

    initialize:function () {
        var self = this;
        this.model.bind("reset", this.render, this);
        this.model.bind("add", function (artist) {
            $(self.el).append(new ArtistListItemView({model:artist}).render().el);
        });
    },

    render:function () {
        // clear the list
        $(this.el).empty();
        console.log("Search results total=" + this.model.models.length);
        if (this.model.models.length >> 0) {
            _.each(this.model.models, function (artist) {
                $(this.el).append(new ArtistListItemView({model:artist}).render().el);
            }, this);
        } else {
            $(this.el).append('<li class="text-center">No Resutls</li>');
        }
        return this;
    }
});

/**
 * This view handles showing an individual artist item in search artist list
 * @type {*}
 */
window.ArtistListItemView = Backbone.View.extend({
    tagName:"li",

    className: "artist-search-results",

    initialize:function () {
        this.model.bind("change", this.render, this);
        this.model.bind("destroy", this.close, this);
    },

    render:function () {
        // pass the model to the template
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }

});