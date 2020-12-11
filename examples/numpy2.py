# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:56:56 2020

@author: srinic
"""
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

mat=np.array([[1,2,3],[4,5,6]])

print(mat)

mat2 = mat-mat

print(mat2)

x = np.random.randint(5, size=(1))
print(x+1)

from numpy import random

#x = random.choice([1, 2, 3, 4,5,6], p=[0.1, 0.25, 0.25, 0.15,0.15,0.1], size=(50))
#print(x)


arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

import matplotlib.pyplot as plt
import seaborn as sns

#sns.distplot(random.normal(size=1000), hist=True)

x = random.binomial(n=10, p=0.5, size=1000)

sns.displot(x)
plt.show()
