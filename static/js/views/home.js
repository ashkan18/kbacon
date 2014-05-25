window.HomeView = Backbone.View.extend({
    el: '#content',

    initialize:function () {
        console.log('Initializing Home View');
        this.render();
    },

    render:function () {
        $(this.el).html(this.template());
        return this;
    }

});