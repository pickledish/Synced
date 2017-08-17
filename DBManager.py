import random
from datetime import datetime, timedelta
from threading import Timer
from firebase import firebase

import os
import redis

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

class DBManager:

	def __init__(self):

		redis.set('available', set(['cat', 'dog', 'helium', 'jane', 'what', 'constant']))
		redis.set('used', set())

		url = "https://synced-3c7d7.firebaseio.com/"
		self.fb = firebase.FirebaseApplication(url, None)

	def getUsed(self):

		return redis.get('used')

	def createKey(self):

		if (not redis.get('available')): return None

		key = random.sample(redis.get('available'), 1).pop()

		s = redis.get('available')
		s.remove(key)
		redis.set('available', s)

		t = redis.get('used')
		t.add(key)
		redis.set('used', t)

		now = datetime.now()
		expiry = now + timedelta(minutes = 10)
		delay = (expiry - now).total_seconds()

		t = Timer(delay, self.removeKey, [key])
		t.start()

		return key

	def removeKey(self, key):

		s = redis.get('available')
		s.add(key)
		redis.set('available', s)

		t = redis.get('used')
		t.remove(key)
		redis.set('used', t)

		try: self.fb.delete('/', key)
		except: pass