# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:16:06 2020

@author: srinic
"""

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def printname(self):
        print("my name is ", self.name)