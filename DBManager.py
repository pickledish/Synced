import random
from datetime import datetime, timedelta
from threading import Timer
from firebase import firebase

class DBManager:

	def __init__(self):

		self.available = set(['cat', 'dog', 'helium', 'jane', 'what', 'constant'])
		self.used = set()

		url = "https://synced-3c7d7.firebaseio.com/"
		self.fb = firebase.FirebaseApplication(url, None)

	def createKey(self):

		if (not self.available): return None

		key = random.sample(self.available, 1).pop()

		self.available.remove(key)
		self.used.add(key)

		now = datetime.now()
		expiry = now + timedelta(minutes = 10)
		delay = (expiry - now).total_seconds()

		t = Timer(delay, self.removeKey, [key])
		t.start()

		return key

	def removeKey(self, key):

		self.used.remove(key)
		self.available.add(key)

		try: self.fb.delete('/', key)
		except: pass