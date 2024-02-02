#!/usr/bin/python3
'''BasicCache Module'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache Class caching system'''

    def put(self, key, item):
        ''' Add key/value pair to cache.
        If either `key` or `item` is None, do nothing. '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Return value stored in `key` of cache.
        If key is None or does not exist in cache, return None. '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
