from flask_script import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
manager = Manager(app)

from SyncedApp import syncedAppBlueprint
app.register_blueprint(syncedAppBlueprint, url_prefix = '')

if __name__ == "__main__":
    manager.run()