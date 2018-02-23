# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:33:31 2018

@author: srinic
"""

from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data[:-1,:], iris.target[:-1]

print(X)

from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression()
logistic.fit(X,y)

print ('Predicted class %s, real class %s' % (logistic.predict(iris.data[:-1,:]),iris.target[:-1]))



print ('Probabilities for each class from 0 to 2:\n %s' % logistic.predict_proba(iris.data[:-1,:]))
 