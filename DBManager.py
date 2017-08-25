import random
from datetime import datetime, timedelta
from threading import Timer
from firebase import firebase

import os
import pickle

from manage import db

class Key(db.Model):

	word = db.Column(db.String(20), primary_key = True)
	used = db.Column(db.Boolean())
	expires = db.Column(db.DateTime())

	def __init__(self, word):

		self.word = word
		self.used = False
		self.expires = None

class DBManager:

	def __init__(self):

		url = "https://synced-3c7d7.firebaseio.com/"
		self.fb = firebase.FirebaseApplication(url, None)

	# Only run this once! By hand!
	def addAllWords(self, sourcePath):

		words = [w.strip() for w in open(sourcePath, 'r').readlines()]

		for w in words:

			key = Key(w)
			db.session.add(key)

		db.session.commit()

	def createKey(self):

		self.refreshKeys()

		available = Key.query.filter_by(used = False)

		if (not available): return None

		key = random.sample(available, 1).pop()

		key.used = True
		key.expires = datetime.now() + timedelta(hours = 24)

		db.session.commit()

		return key.word

	def refreshKeys(self):

		used = Key.query.filter_by(used = True)

		for key in used:

			if (key.expires < datetime.now()):

				key.used = False
				key.expires = None

				self.fb.delete('/', key.word)

		db.session.commit()


