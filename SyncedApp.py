#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, Blueprint, render_template
from DBManager import DBManager

#----------------------------------------------------------------------------#
# App Config
#----------------------------------------------------------------------------#

syncedAppBlueprint = Blueprint('syncedApp', __name__,
	template_folder = 'templates', static_folder = 'static')

dbManager = DBManager()

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

	key = dbManager.createKey()

	if (key is None): 
		return render_template("error.html", errorText = getKeyErr)

	return render_template("success.html", key = key)

@syncedAppBlueprint.route('/<key>')
def viewEditor(key):

	if (key not in dbManager.used):

		return render_template("error.html", errorText = missingKeyErr)

	return render_template("editor.html", key = key)







