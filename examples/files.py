# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:38:11 2020

@author: srinic
"""

import os


f = open("hello.txt","at")
f.write("sample text")
f.close()

f= open("hello.txt", "rt")
txt=f.read()
print(txt)
f.close()

os.remove("hello.txt")


