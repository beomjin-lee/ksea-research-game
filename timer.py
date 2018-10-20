import time
import ctypes

def timer(minutes):
    seconds = minutes * 60
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
    time.sleep(1)
timer(0.1) #would want enter in hours not in seconds
    



print ('Hello')