# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 08:51:48 2018

@author: srinic
"""
import csv
import numpy
from pandas import read_csv

filename = '..\\TWTR.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x)
print(data.shape)
print(data)


names = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
data = read_csv(filename)
print(data.shape)
delta = data['High'] - data['Low']
print('%s' % delta)

#import matplotlib.pyplot as plt
#plt.xlabel('Date')
#plt.ylabel('Volume')

#plt.scatter(data['Date'], data['Volume'])
#plt.scatter(data['Date'], delta)
#plt.show()

X = data.iloc[0:1078,1:7]
y = data.iloc[1:,1:2]
#print(X)
#print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

from sklearn.linear_model import LinearRegression

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))

intercept = regression_model.intercept_[0]

print("The intercept for our model is {}".format(intercept))

print(regression_model.score(X_test, y_test))

from sklearn.metrics import mean_squared_error

y_predict = regression_model.predict(X_test)

regression_model_mse = mean_squared_error(y_predict, y_test)

print(regression_model_mse)

import math

print(math.sqrt(regression_model_mse))

prdval = regression_model.predict([[33.43,33.45,31.63,32.11,32.11,29128100]])

print(prdval)








