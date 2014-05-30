describe("Test ArtistSearchCollection", function () {
    var artistModel;

    beforeEach(function () {
        artistModel = new ArtistSearchCollection();
    });

    it("should make the correct server request", function() {


        // Spy on jQuery's ajax method
        var spy = sinon.spy(jQuery, 'ajax');

        artistModel.fetch({
            type: 'GET',
            data: {'query': 'test'}
        });

        expect(spy.getCall(0).args[0].url).toBe("../api/artists/search");
        expect(spy.getCall(0).args[0].data.query).toBe("test");
        expect(spy.getCall(0).args[0].type).toBe("GET");

        // Restore jQuery.ajax to normal
        jQuery.ajax.restore();
    });
});
