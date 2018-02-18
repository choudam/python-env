# -*- coding: utf-8 -*-

import threading
import ctypes
import time

w32 = ctypes.windll.kernel32

THREAD_PRIORITY_NORMAL = 0
THREAD_PRIORITY_ABOVE_NORMAL = 1
THREAD_PRIORITY_HIGHEST = 2
HIGH_PRIORITY_CLASS = 0x00000080
NORMAL_PRIORITY_CLASS = 0x00000020


result = w32.SetPriorityClass(w32.GetCurrentProcess(), HIGH_PRIORITY_CLASS)
if not result:
    print ('Failed to set priority of thread', w32.GetLastError())
        
startTime = time.time()
finalsum = 0
lock = threading.Lock()

def worker(num,bi,ei):
    global finalsum
    global lock 
    result = w32.SetThreadPriority(w32.GetCurrentThread(), THREAD_PRIORITY_HIGHEST)
    if not result:
        print ('Failed to set priority of thread', w32.GetLastError())
          
    ei+=1
    tempsum = 0
#    i = bi
#    while(i < ei):
#        tempsum += i
#        i += 1
    for i in range(bi,ei):
        tempsum = tempsum + i
    lock.acquire()
    finalsum += tempsum
    lock.release()
    return

threadscount = 4
numcount = 1000000000
ransize = int(numcount / threadscount)
print('ransize %d' % ransize)

threads = []
for i in range(threadscount):
    bi = ransize * i + 1
    ei = bi + ransize - 1 
    t = threading.Thread(target=worker, args=(i,bi,ei,))
    threads.append(t)
    t.start()
    

# join threads
for i in range(threadscount):
    threads[i].join()
    
print(finalsum)
print('Time elapsed:', time.time() - startTime)


    
    


