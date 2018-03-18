#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:21:50 2017
# based on work done by yucedagonurcan hack on github - https://github.com/yucedagonurcan/RNN_LSTM_for_Google_Stocks/blob/master/RNN_LSTM_Google_Stocks.py
@author: pdavis39
"""
#import lib and data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

training_set=pd.read_csv('/media/nvidia/JetsonSSD-250/sandbox/dev/bitcoin-price-api/train_btc.csv')
training_set=training_set.iloc[:,1:2].values

#feat scaling
from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
training_set=sc.fit_transform(training_set)
Xtrain=training_set[0:1582]
Ytrain=training_set[1:1583]


#shaping data
Xtrain=np.reshape(Xtrain,(1582,1,1))

#RNN model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

reg=Sequential()

reg.add(LSTM(units=4,activation='sigmoid',input_shape=(None,1)))

reg.add(Dense(units=1))

reg.compile(optimizer='adam',loss='mean_squared_error')

reg.fit(Xtrain,Ytrain,batch_size=32,epochs=200)

test_set=pd.read_csv('/media/nvidia/JetsonSSD-250/sandbox/dev/bitcoin-price-api/test_btc.csv')
real_btc_price=test_set.iloc[:,1:2].values

#getting the prediction BTC
inputs=real_btc_price
inputs=sc.transform(inputs)

# Reshaping for keras [reshape into 3 dimensions, [batch_size, timesteps, input_dim]]

inputs=np.reshape(inputs,(40,1,1))

predicted=reg.predict(inputs)

predicted=sc.inverse_transform(predicted)

plt.plot(real_btc_price,color='red',label='Real BTC price')
plt.plot(predicted,color='blue',label='predicted BTC price')
plt.title('BTC price prediction')
plt.xlabel('Days')
plt.ylabel('BTC price')
plt.legend()
plt.show()

#getting the real btc price
RST=pd.read_csv('/media/nvidia/JetsonSSD-250/sandbox/dev/bitcoin-price-api/train_btc.csv')
RST=RST.iloc[:,1:2].values
#predicted btc price 
predict_btc_price_train=reg.predict(Xtrain)
predict_btc_price_train=sc.inverse_transform(predict_btc_price_train)

plt.plot(RST,color='red',label='Real BTC price')
plt.plot(predict_btc_price_train,color='blue',label='predicted BTC price')
plt.title('BTC price prediction')
plt.xlabel('Days')
plt.ylabel('BTC price')
plt.legend()
plt.show()

#evaluate RNN
import math
from sklearn.metrics import mean_squared_error 
rmse=math.sqrt(mean_squared_error(real_btc_price,predicted))
error=rmse/800 #mean error devided by the avg

