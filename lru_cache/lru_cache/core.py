from collections import OrderedDict
import time


class LRUCache(object):
	"""
	@brief      Class for LRU cache.
	"""
	def __init__(self, max_size=1024,expiration=None):
		self.max_size = max_size
		self.expiration = expiration
		self.values = {}
		self.access_order = OrderedDict()

	def __remove_expired(self):
		curr_time = time.time()
		for key, access_time in self.access_order.items():
			if access_time + self.expiration <= curr_time:
				del self.values[key]
				del self.access_order[key]

	def __getitem__(self, key):
		"""
		@brief      Get object with key as 'key'
		
		@param      self  The object
		@param      key   The key
		
		@return     The value associated with 'key'
		"""
		if self.expiration:
			self.__remove_expired()
		if key in self.values:
			del self.access_order[key]
			self.access_order[key] = time.time()
			return self.values[key]
		return None

	def __contains__(self, key):
		if self.expiration:
			self.__remove_expired()
		return key in self.values
	
	def __insertitem(self, key, value):
		if key in self.values:
			del self.access_order[key]
		self.access_order[key] = time.time()
		self.values[key] = value

	def __setitem__(self, key, value):
		"""
		@brief      Sets a new key, value in the cache
		
		@param      self   The object
		@param      key    The key
		@param      value  The value	
		"""
		if self.expiration:
			self.__remove_expired()
		
		if len(self.values) == self.max_size:
			old_key, old_timestamp = self.access_order.popitem(last=False)
			del self.values[old_key]
		self.__insertitem(key, value)

	def __delete__(self, key):
		"""
		@brief      Delete value with key as 'key'
		
		@param      self  The object
		@param      key   The key		
		"""
		if key in self.values:
			del self.values[key]
			del self.access_order[key]

	def size(self):
		if self.expiration:
			self.__remove_expired()
		
		return len(self.values)

	def capacity(self):
		return self.max_size