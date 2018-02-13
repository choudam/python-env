import pandas
import logging
import sys
import io
import math

def Nprime(cnt:int):
    nextNumber = 2;
    primelist = [];

    while cnt > 0:
            isprime = True;
            sqrtnum = math.sqrt(nextNumber);
            for prm in primelist:
                if (nextNumber % prm == 0):
                    isprime = False;
                    break;
                if (prm >= sqrtnum):
                    break;
            if (isprime):
                primelist.append(nextNumber);
                print(cnt,':', nextNumber);
                cnt-=1
            nextNumber+=1;
    return primelist;
#print(primelist);



cnt =0;
cnt = int(input("How many prime numbers you want:"));

print (Nprime(cnt));

