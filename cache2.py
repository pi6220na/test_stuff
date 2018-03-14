import datetime
import random
import pprint
import numpy

########################################################################
class MyCache:
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 10

    # ----------------------------------------------------------------------
    def __contains__(self, key):
        """
        Returns True or False depending on whether or not the key is in the
        cache
        """
        return key in self.cache

    # ----------------------------------------------------------------------
    def update(self, key, value):
        """
        Update the cache dictionary and optionally remove the oldest item
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()

        dt_now = datetime.datetime.now()
        dt_obj = datetime.datetime.strptime(str(dt_now),
                                   '%Y-%m-%d %H:%M:%S.%f')
        millisec = dt_obj.timestamp() * 1000

        self.cache[key] = {'date_accessed': millisec,
                           'value': value}

        # self.cache[key] = {'date_accessed': datetime.datetime.now(),
        #                    'value': value}

        # self.cache[key] = {'date_accessed': numpy.datetime64(),
        #                    'value': value}

    # ----------------------------------------------------------------------
    def remove_oldest(self):
        """
        Remove the entry that has the oldest accessed date
        """
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry][
                'date_accessed']:
                oldest_entry = key
        self.cache.pop(oldest_entry)

    # ----------------------------------------------------------------------
    @property
    def size(self):
        """
        Return the size of the cache
        """
        return len(self.cache)

    def get_cache(self):
        return self.cache

if __name__ == '__main__':

    pp = pprint.PrettyPrinter(indent=4)

    # Test the cache
    keys = ['test', 'red', 'fox', 'fence', 'junk',
            'other', 'alpha', 'bravo', 'cal', 'devo',
            'ele']
    s = 'abcdefghijklmnop'
    cache = MyCache()
    for i, key in enumerate(keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(s) for i in range(20)])
            cache.update(key, value)
            print('key = ' + key + ' value = ' + value)
        print("#%s iterations, #%s cached entries" % (i+1, cache.size))
    print()

    cache.update('mem', 'asdfasdf')

    pCache = cache.get_cache()
    for i, key in enumerate(pCache):
        print('key = %s  value = %s' % (i, key))

    pp.pprint(pCache)