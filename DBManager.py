import random
from datetime import datetime, timedelta
from threading import Timer
from firebase import firebase

import os
import pickle

class DBManager:

	def __init__(self, sourcePath):

		return

		self.available = RedisSet('available')
		self.used = RedisSet('used')

		words = [w.strip() for w in open(sourcePath, 'r').readlines()]

		self.available.storeSet(set(words))
		self.used.storeSet(set())

		url = "https://synced-3c7d7.firebaseio.com/"
		self.fb = firebase.FirebaseApplication(url, None)

	def createKey(self):

		return "hello"

		available = self.available.getSet()

		if (not available): return None

		key = random.sample(available, 1).pop()

		self.available.removeKey(key)
		self.used.addKey(key)

		now = datetime.now()
		expiry = now + timedelta(hours = 24)
		delay = (expiry - now).total_seconds()

		t = Timer(delay, self.removeKey, [key])
		t.start()

		return key

	def removeKey(self, key):

		return

		self.used.removeKey(key)
		self.available.addKey(key)

		try: self.fb.delete('/', key)
		except: pass