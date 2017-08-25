from flask_script import Manager
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

from SyncedApp import syncedAppBlueprint

app = Flask(__name__)
app.register_blueprint(syncedAppBlueprint, url_prefix = '')
app.config.from_object('config')

db = SQLAlchemy(app)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()