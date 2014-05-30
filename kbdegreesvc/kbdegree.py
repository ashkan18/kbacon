from kbdegreesvc import app

__author__ = 'Ashkan'

if __name__ == '__main__':
    # in case we want to run this locally, mostly for debug reasons
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

