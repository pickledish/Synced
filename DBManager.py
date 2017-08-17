import random
from datetime import datetime, timedelta
from threading import Timer
from firebase import firebase

import os
import redis
import pickle

conn = redis.from_url(os.getenv('REDISTOGO_URL'))

class RedisSet:

	def __init__(self, name):

		self.name = name
		self.storeSet(set())

	def getSet(self):

		pickled = conn.get(self.name)
		return pickle.loads(pickled)

	def storeSet(self, newSet):

		pickled = pickle.dumps(newSet)
		conn.set(self.name, pickled)

	def addKey(self, key):

		toStore = self.getSet()
		toStore.add(key)
		self.storeSet(toStore)

	def removeKey(self, key):

		toStore = self.getSet()
		toStore.remove(key)
		self.storeSet(toStore)

class DBManager:

	def __init__(self):

		self.available = RedisSet('available')
		self.used = RedisSet('used')

		self.available.storeSet(set(['cat', 'dog', 'helium', 'jane', 'what', 'constant']))
		self.used.storeSet(set())

		url = "https://synced-3c7d7.firebaseio.com/"
		self.fb = firebase.FirebaseApplication(url, None)

	def createKey(self):

		available = self.available.getSet()

		if (not available): return None

		key = random.sample(available, 1).pop()

		self.available.removeKey(key)
		self.used.addKey(key)

		now = datetime.now()
		expiry = now + timedelta(minutes = 10)
		delay = (expiry - now).total_seconds()

		t = Timer(delay, self.removeKey, [key])
		t.start()

		return key

	def removeKey(self, key):

		self.used.removeKey(key)
		self.available.addKey(key)

		try: self.fb.delete('/', key)
		except: pass