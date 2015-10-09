import urllib2 
from multiprocessing.dummy import Pool as ThreadPool 
import time
urls = [
    'http://www.python.org', 
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc.. 
    ]

time1 = time.time()
# Make the Pool of workers
pool = ThreadPool(15) 
# Open the urls in their own threads
# and return the results
results = pool.map(urllib2.urlopen, urls)
print results
#close the pool and wait for the work to finish 
pool.close() 
pool.join() 
time2 = time.time()
print str(time2-time1)