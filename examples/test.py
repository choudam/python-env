# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:45:18 2020

@author: srinic
"""

import person as pr
        
        
p1=pr.Person("John",36)
print(p1.name)
print(p1.age)

print(p1)

p1.printname()

del p1

import mynumbers as mn

            

myobj = mn.mynumbers()
myiter=iter(myobj)

[print(x) for x in myiter]

del myiter
del myobj

myobj = mn.mynumbers(100)
myiter=iter(myobj)

[print(x) for x in myiter]
print(myiter)



import datetime as dt

x=dt.datetime.now()
print(x)

import json 

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

jx=json.dumps(x)

print(jx)
jp=json.loads(jx)

print(jp)



import re

txt="The rain in Spain"
x=re.findall("ai",txt)
print(x)

s=re.search("ai",txt)
print(s.start())

t = re.split("\s",txt)
print(t)




