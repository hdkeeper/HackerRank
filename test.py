from NamedAtomicLock import NamedAtomicLock
from time import sleep

myLock = NamedAtomicLock('myLock')
if myLock.acquire(timeout=15):
    print('Processing')
    sleep(5)

myLock.release()
