window.HomeView = Backbone.View.extend({
    el: '#content',
    /**
     * This class handles showing the content of the main page
     */
    initialize:function () {
        console.log('Initializing Home View');
        this.render();
    },

    render:function () {
        $(this.el).html(this.template());
        return this;
    }

});