# Compare Version Numbers

### Question Statement:

At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria: 

1. Simplicity. Integration needs to be dead simple.
2. Resilient to network failures or crashes.
3. Near real time replication of data across Geolocation. Writes need to be in real time.
4. Data consistency across regions
5. Locality of reference, data should almost always be available from the closest region
6. Flexible Schema
7. Cache can expire

*************************

### Approach

The LRUCache uses two data structures of pre-defined capacity: 
1. An unordered dict which stores the <key,value> pairs for the data
2. An ordered dict which stores <key,timestamp> pairs for the stored objects. 

#### Get Item
If the given key exists in the cache, return the value associated with the key and update key to be the most recently used item.

#### Set Item
If cache has enough capacity to accomodate new item, then insert it into the cache as the most recently used. If the cache is full, then remove the least recently used item and then insert the new item.

To allow for cache expiration, lazy cache cleanup is implemented wherein the expired items are removed on getitem, setitem and size() calls to the LRUCache object.

The design of the LRU covers simplicity, flexibly schema and cache expiration.

To allow for locality of reference there needs to be several such instances of the cache operating in different Geo Locations with a DNS server between the client and the different cache servers such that the DNS server routes a client request to the nearest available cache server.

To implement data consistency across regions:
Each <key,value> pair has an individual lock (for larger cache sizes, chunks of the cache can have a lock instead of imposing finer granularity).
Writes to a cache server need to be updated in real time across the different geo locations. This can be achieved by sending a write request to the main server which sends a write request to each cache server by acquiring a lock to the specific key value that needs to be updated.

For network failures/crashes:
Implement a master/slave based architecture at each cache server in which data is kept consistent between them. If the master crashes the slave behaves as the master. 

There is a clear tradeoff between availability and consistency of data across regions. If availability is more favourably, more slaves can be kept.

### API
```python
from lru_cache import LRUCache

cache = LRUCache(maxsize=2)
cache['a'] = 123
cache['b'] = {'x':'y'}
print(cache['a'])
cache['c'] = [1,2,3]
print(cache['a']) # None
print(cache['b']) # {'x':'y'}
print(cache['c']) # [1,2,3]

```

### How To Test:

```
$ python -m unittest tests/tests_lru_cache.py
```

Python version used: **Python 3.6.4**
