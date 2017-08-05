from flask_script import Manager
from flask import Flask, url_for

from NewApp import newAppBlueprint

app = Flask(__name__)
app.register_blueprint(newAppBlueprint, url_prefix = '')
app.config.from_object('config')

manager = Manager(app)

if __name__ == "__main__":
    manager.run()