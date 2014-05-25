
/* Wasn't able to find a way to pass files as templates in backbone,
  ended up using this which basically gets the file by just making a get call to template file
  and then passes the content of the file as the view's template

  NOTE: this only works when template file name is same as View name
*/
window.templateLoader = {

    load: function(views, callback) {

        var deferreds = [];

        $.each(views, function(index, view) {
            if (window[view]) {
                deferreds.push($.get('tpl/' + view + '.html', function(data) {
                    window[view].prototype.template = _.template(data);
                }, 'html'));
            } else {
                alert(view + " not found");
            }
        });

        $.when.apply(null, deferreds).done(callback);
    }

};