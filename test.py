# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 09:16:21 2021

@author: Srujan Gupta
"""
from math import sqrt
import numpy as np
from matplotlib import pyplot
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error

 
#setting random seed
np.random.seed(42)

# load dataset
folder = "C:/Users/Srujan Gupta/"
df = pd.read_csv("model_dataset.csv")


# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(df)

 
# split into input and outputs
x = scaled[:,:-1]
y = scaled[:,-1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# reshape input to be 3D [samples, timesteps, features]
x_train = x_train.reshape((x_train.shape[0],1,x_train.shape[1])) ##should the last one be x_train.shape[1]-1 ???
x_test = x_test.reshape((x_test.shape[0],1,x_test.shape[1])) ##should the last one be x_train.shape[1]-1 ???
 
# design network
model = Sequential()
model.add(LSTM(50, input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=50, batch_size=20, verbose=1, shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()
 
# make a prediction
yhat = model.predict(x_test)
x_test = x_test.reshape((x_test.shape[0], x_test.shape[2]))

# invert scaling for forecast
inv_yhat = np.concatenate((x_test[:, :],yhat), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,-1]

# invert scaling for actual
y_test = y_test.reshape((len(y_test), 1))
inv_y = np.concatenate((x_test[:, :],y_test), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,-1]

# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
#print('Test RMSE: %.3f' % rmse)
df["Spots"].mean() ##Answer is 24
print("RMSE:",rmse,"MAE:",mean_absolute_error(inv_y,inv_yhat),"Median AE:",median_absolute_error(inv_y, inv_yhat)) ##16.23, 12.98, 10.61