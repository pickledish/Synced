#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import random

from flask import Flask, Blueprint, render_template
from werkzeug.contrib.cache import SimpleCache

#----------------------------------------------------------------------------#
# App Config
#----------------------------------------------------------------------------#

syncedAppBlueprint = Blueprint('syncedApp', __name__,
	template_folder = 'templates', static_folder = 'static')

cache = SimpleCache()

wordList = ['cat', 'dog', 'helium', 'jane', 'what', 'constant', 'of']
cache.set('availableWords', set(wordList))
cache.set('usedWords', set())

getKeyErr = "There are no available keys! Please try again?"
missingKeyErr = "Sadly that key does not exist!"

#----------------------------------------------------------------------------#
# Controllers
#----------------------------------------------------------------------------#

@syncedAppBlueprint.route('/')
def index():

	return render_template("index.html")

@syncedAppBlueprint.route('/create')
def newEditor():

	available = cache.get('availableWords')
	used = cache.get('usedWords')

	if (not available):
		return render_template("error.html", errorText = getKeyErr)

	key = random.sample(available, 1).pop()

	available.remove(key)
	used.add(key)

	cache.set('availableWords', available)
	cache.set('usedWords', used)

	return render_template("created.html", key = key)

@syncedAppBlueprint.route('/<key>')
def viewEditor(key):

	used = cache.get('usedWords')

	if (not used or key not in used):
		return render_template("error.html", errorText = missingKeyErr)

	return render_template("editor.html", key = key)







