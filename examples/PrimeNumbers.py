import math
import time
#import threading


def Nprime(cnt:int, segsize:int):
    nextNumber = 2;
    primelist = [];

    while cnt > 0:
            isprime = True;
            endnum = nextNumber - 1;
            for prm in range(2, endnum):
                if (nextNumber % prm == 0):
                    isprime = False;
                    break;
                if (prm >= endnum):
                    break;
            if (isprime):
                primelist.append(nextNumber);
                if( cnt % segsize == 0):
                    print(cnt,':', nextNumber);
                cnt-=1
            nextNumber+=1;
    return primelist;

def NprimeSqrt(cnt:int, segsize:int):
    nextNumber = 2;
    primelist = [];

    while cnt > 0:
            isprime = True;
            endnum = int(math.sqrt(nextNumber)) + 1;
            for prm in range(2, endnum):
                if (nextNumber % prm == 0):
                    isprime = False;
                    break;
                if (prm >= endnum):
                    break;
            if (isprime):
                primelist.append(nextNumber);
                if( cnt % segsize == 0):
                    print(cnt,':', nextNumber);
                cnt-=1
            nextNumber+=1;
    return primelist;


def NprimeSqrtPrimes(cnt:int, segsize:int):
    nextNumber = 2;
    primelist = [];

    while cnt > 0:
            isprime = True;
            endnum = math.sqrt(nextNumber);
            for prm in primelist:
                if (nextNumber % prm == 0):
                    isprime = False;
                    break;
                if (prm >= endnum):
                    break;
            if (isprime):
                primelist.append(nextNumber);
                if( cnt % segsize == 0):
                    print(cnt,':', nextNumber);
                cnt-=1
            nextNumber+=1;
    return primelist;

#nextNumber = 2;
#primelist = [];
#lock = threading.Lock()
#primenumcount = 0
# 
#def NprimeSqrtPrimesMultiThreads(cnt:int):
#    global primenumcount
#    global nextNumber
#    global primelist
#    primenumcount = cnt
#    nextNumber = 2;
#    primelist = [];
#    
#    threadscount = 8
#    threads = []
#    for i in range(threadscount):
#        t = threading.Thread(target=worker, args=(i,))
#        threads.append(t)
#        t.start()
#
#    for i in range(threadscount):
#        threads[i].join()
#    return;
#
#def worker(thid:int):
#    global primenumcount
#    global nextNumber
#    global primelist
#    while primenumcount > 0:
#            isprime = True;
#            endnum = math.sqrt(nextNumber);
#            prmidx = 0
#            while(isprime):
#                if (nextNumber % primelist[prmidx] == 0):
#                    isprime = False;
#                    break;
#                if (primelist[prmidx] >= endnum):
#                    break;
#                if (prmidx < primelist.count):
#                    prmidx += 1
#                
#            
#            lock.acquire()
#            if (isprime):                
#                primelist.append(nextNumber);
#                if( primenumcount % 10000 == 0):
#                    print(thid, '-', primenumcount,':', nextNumber);
#                primenumcount-=1                
#            nextNumber+=1;
#            lock.release()
#    return
#    


cnt = 10000
segsize = 1000
#cnt = int(input("How many prime numbers you want:"));

startTime = time.time()
Nprime(cnt,segsize);
print('Time elapsed for Nprime: %d - %f \n' % (cnt, time.time() - startTime))

startTime = time.time()
NprimeSqrt(cnt,segsize);
print('Time elapsed for NprimeSqrt: %d - %f \n' % (cnt, time.time() - startTime))

startTime = time.time()
NprimeSqrtPrimes(cnt,segsize);
print('Time elapsed for NprimeSqrtPrimes: %d - %f \n' % (cnt, time.time() - startTime))


#startTime = time.time()
#NprimeSqrtPrimesMultiThreads(cnt);
#print('Time elapsed for NprimeSqrtPrimesMultiThreads: %d - %f \n' % (cnt, time.time() - startTime))



