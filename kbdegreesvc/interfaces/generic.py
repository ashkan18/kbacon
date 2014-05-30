from kbdegreesvc import app

__author__ = 'Ashkan'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
