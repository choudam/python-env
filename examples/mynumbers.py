# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:13:06 2020

@author: srinic
"""

class mynumbers:
    def __init__(self,n=10):
        self.n=n
        
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=self.n:
            x= self.a
            self.a +=1
            return x
        else:
            raise StopIteration