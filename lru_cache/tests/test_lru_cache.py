import unittest,time
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_basic(self):
        """
        @brief      Test getitem/setitem of the LRUCache object
        
        @param      self  The object
        """
        cache = LRUCache(max_size=3)
        cache['a'] = 1
        self.assertEqual(cache['a'], 1)

    def test_size(self):
        """
        @brief      Test size method of the LRUCache object
        
        @param      self  The object
        """
        cache = LRUCache(max_size=3)
        cache['a'] = 1
        cache['b'] = "random"
        self.assertEqual(cache.size(), 2)

    def test_expiration(self):
        """
        @brief      Test cache expiration of the LRUCache object
        
        @param      self  The object
        """
        cache = LRUCache(max_size=3,expiration=3)
        cache['a'] = 1
        time.sleep(5)
        self.assertEqual(cache['a'], None)


if __name__ == '__main__':
    unittest.main()