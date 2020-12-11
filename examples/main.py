# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math as m


l1 = np.random.rand(100)
print(l1)

arr1 = [1,2,3,4,5,6]
for e1 in arr1:
    print(m.log2(e1*e1))
    
for i in range(len(arr1)):
    print(i, arr1[i])
    
i=0
while(i<len(arr1)):
    print(arr1[i])
    i=i+1
    
[ print(x) for x in arr1]

[ print(x) for x in arr1 if x>4]

list2 = [ m.sqrt(x)/2 for x in range(100)]

print(list2)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)

print(thistuple[2:4])

tuple1 = ("a", "b", "c")
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3)

print(tuple3.index(3))

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple","banana","cherry"}
set2 ={"pineapple","mango","papaya"}
thisset.update(set2)
print(thisset)

dict2= { "brand":"Ford", "model":"Mustang", "year":1954}
print(dict2)
print(len(dict2))

print(dict2.keys())

print(dict2.values())

dict2["color"]="red"

print(dict2.keys())

print(dict2.values())

dict3 = dict(dict2)

del dict2["brand"]

print(dict2.keys())

print(dict2.values())

[ print(x) for x in dict2]
[ print(dict2[x]) for x in dict2]


print(dict3)


x =100
y=200

if ( x>y):
    print(x)
else:
    print(y)
    

def sum_of_first_n(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s

print(sum_of_first_n(10))

def factorial(n):
    if n <=1: 
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(7))


def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(2)
mytripler= myfunc(3)

print(mydoubler(11))
print(mytripler(11))

import json

y= json.dumps(dict2)

print(y)



