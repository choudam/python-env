# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:19:24 2020

@author: srinic
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:17:22 2020

@author: srinic
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
#from sklearn.model_selection import model_selection


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

dataset = pd.read_csv(r"d:\python\stockdata\msft.csv", index_col="Date",parse_dates=True)
dataset=dataset.drop("AdjClose", axis="columns")

#inspect data

#print(dataset.head())
#print(dataset.tail())
#print(dataset.isna().any())
#print(dataset.info())

#plot data 

dataset["Close"].plot(figsize=(16,6))


dataset["Volume"] = dataset["Volume"].astype(float)
#print(dataset.info())

rolling5 = dataset.rolling(5).mean()
rolling20 = dataset.rolling(20).mean()
rolling50 = dataset.rolling(50).mean()
rolling200 = dataset.rolling(200).mean()
rolling52weeklow= dataset.rolling(200).min()
rolling52weekhigh= dataset.rolling(200).max()

dataset = pd.concat([dataset, rolling5,rolling20,rolling50,rolling200,rolling52weeklow,rolling52weekhigh], axis=1)

dataset = dataset.dropna(how="any",axis=0)

print(dataset.info())
print(dataset.head(50))



#print(rolling5.head(20))
rolling5["Close"].plot(figsize=(16,6))
rolling20["Close"].plot(figsize=(16,6))
rolling50["Close"].plot(figsize=(16,6))
rolling200["Close"].plot(figsize=(16,6))
rolling52weeklow["Close"].plot(figsize=(16,6))
rolling52weekhigh["Close"].plot(figsize=(16,6))

plt.show()

#data preprocessing

training_column="Close"
feature_size=5
#training_set = pd.DataFrame(dataset[training_column])
#Feature scaling
sc=MinMaxScaler(feature_range=(0,1))
training_set = sc.fit_transform(dataset.to_numpy())
#print(training_set.head(20))

print("training set zise: ", training_set.shape)


# create Features
X=[]
y=[]

pasthistory=20

for i in range(pasthistory, training_set.shape[0]-1):
    X.append(training_set[i-pasthistory:i,:])
    y.append(training_set[i,:])

X,y=np.array(X),np.array(y)
print(X.shape)
#reshaping
X=np.reshape(X,(X.shape[0],X.shape[1]*X.shape[2]))

print(X.shape)


#split train and test set
train_size=1000
test_size=30
X_train=X[-train_size:-test_size,:]
X_test=X[-test_size:,:]
X_train=np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))
X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
print("X_train shape: ", X_train.shape)
y_train=y[-train_size:-test_size,:]
y_test=y[-test_size:,:]
print("y_test shape: ", y_test.shape)

#X_train,X_test,y_train,y_test=model_selection.train_test_split(X,y,train_size=0.65,test_size=0.35,random_state=101)
#print(X_train)
#print(X_test)
#print(y_train)
#print(y_test)

#initalize RNN
regressor = Sequential()

hiddenunits=64
epochs_num=100
output_count=5
#layer 1 (input layer)
regressor.add(LSTM(units=hiddenunits,return_sequences=True,input_shape=(X_train.shape[1],1)))
#regressor.add(Dropout(0.2))

#layer 2 -(hidden layer 1)
regressor.add(LSTM(units=int(hiddenunits/2), return_sequences=True))
#regressor.add(Dropout(0.2))

#layer 3 -(hidden layer 2)
regressor.add(LSTM(units=int(hiddenunits/4), return_sequences=True))
#regressor.add(Dropout(0.2))

#layer 4 -(hidden layer 3)
regressor.add(LSTM(units=int(hiddenunits/8)))
#regressor.add(Dropout(0.2))

#layer 5 - output layer
regressor.add(Dense(units=output_count))

#complie and generate model
regressor.compile(optimizer="adam", loss='mean_squared_error')

#Fit model
y_train_all = y_train[:,0:output_count]
#y_train_all = y_train_all.reshape(y_train_close.shape[0],5)
print(y_train_all.shape)
print(X_train.shape)
regressor.fit(X_train,y_train_all,epochs=epochs_num,batch_size=32)



#generate test set

#predict future

y_pred_all = regressor.predict(X_test)
#print(y_pred)

print("y_pred shape: ", y_pred_all.shape)

y_pred1=np.copy(y_test)
display_col=3
#print(y_pred1)
y_pred1[:,display_col]=y_pred_all[:,display_col]
#print(y_pred1)

#graph predicted stock price

y_test_price = sc.inverse_transform(pd.DataFrame(y_test))[:,display_col]
y_pred_price=sc.inverse_transform(pd.DataFrame(y_pred1))[:,display_col]

print(y_test_price)
print(y_pred_price)




#y_test_price = y_test
#y_pred_price=y_pred
#print(y_train_close)
#print(y_pred)

#plt.plot(y_test[:,3], color="red", label="real price") 
#plt.plot(y_pred, color="blue", label="predicted price") 

plt.plot(y_test_price, color="red", label="real price") 
plt.plot(y_pred_price, color="blue", label="predicted price") 
plt.title("Stock Price Prediction") 
plt.xlabel("Time") 
plt.ylabel("Stock Price")
plt.legend()
plt.show()





