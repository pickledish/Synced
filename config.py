import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# http://clsc.net/tools-old/random-string-generator.php
SECRET_KEY = 'my precious'

SOURCE_PATH = 'google-10000-english-usa-no-swears-medium.txt'

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

FIREBASE_URL = "https://synced-3c7d7.firebaseio.com/"