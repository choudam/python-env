# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 08:47:12 2018

@author: srinic
"""

import numpy
print('numpy {}'.format(numpy.__version__))

import matplotlib.pyplot as plt

import pandas


#mydict = {'a': 1, 'b': 2, 'c': 3}
#print("A value: %d" % mydict['a'] )
#mydict['a'] = 11 
#print("A value: %d" % mydict['a']) 
#print("Keys: %s" % mydict.keys() )
#print("Values: %s" % mydict.values() )
#for key in mydict.keys(): 
#    print(mydict[key])
#
#mylist = [[1,2,3],[4,5,6]]
#myarray = numpy.array(mylist)
#print(myarray)
#print(myarray.shape)

myarray1 = numpy.array([1,2,3])
myarray2 = numpy.array([4,5,6])
print(myarray1 + myarray2)
print(myarray1 * myarray2)

#plt.plot(myarray1)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
#plt.draw()

plt.scatter(myarray1, myarray2)
plt.show()

rownames =['a','b','c']
mydata = pandas.Series(myarray1, index=rownames)
print(mydata)


myarray = numpy.array([[1,2,3],[4,5,6]])
rownames = ['a','b']
colnames = ['one','two','three']
mydataframe = pandas.DataFrame(myarray,index=rownames,columns=colnames)
print(mydataframe)
print(mydataframe.one)

print('%s' % mydataframe.one)










