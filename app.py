import os
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

if os.getenv('APP_CONFIG'):
    app.config.from_envvar('APP_CONFIG')
else:
    app_env = os.getenv('APP_ENV', 'Dev')
    app.config.from_object("config.{}Config".format(app_env))

HOSTNAME = subprocess.check_output("hostname").strip().decode('utf-8')


@app.route('/')
def index():
    greeting = "Hello there! Hope you're enjoying Kubernetes!"
    return render_template('index.html', greeting=greeting, hostname=HOSTNAME)


@app.route('/version')
def version():
    return app.config['APP_VERSION']


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=app.config['PORT'], debug=app.config['DEBUG'])