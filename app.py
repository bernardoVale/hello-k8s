import os
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.{}Config'.format(os.getenv('APP_ENV', 'Dev')))


@app.route('/')
def index():
    hostname = app.config['HOSTNAME']
    return "Hello there! Hope you're enjoying Kubernetes. You're running on {}".format(hostname)


@app.route('/version')
def version():
    return app.config['APP_VERSION']


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=app.config['PORT'], debug=app.config['DEBUG'])