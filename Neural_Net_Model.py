#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 23:44:54 2018

@author: reddy
"""
"""
This code contains neural network code. ANN were one of the models used to experiment with the data. Although the results were comparably not good. In future we can improve this by using bayesian optimization.
"""
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.ensemble import RandomForestRegressor

import pandas as pd
X = pd.read_csv("model_train.csv")
X = X.iloc[:,1:]
X = X[(X.iloc[:,6]!=0) & (X.iloc[:,1]!=0)]
X = X.fillna(X.mean())
X_host= pd.get_dummies(X["superhost"])

X = pd.concat([X,X_host],axis =1)
X = X.drop("superhost",axis = 1)
X = X.iloc[:,2:]

from sklearn.model_selection import train_test_split

#Model for Predicting Overall rating
Overall_rating_X = X.iloc[:,:6]
Overall_rating_y = X.iloc[:,6]
X_train, X_test, y_train, y_test = train_test_split(Overall_rating_X, Overall_rating_y, test_size=0.2, random_state=48)

model = Sequential()
model.add(Dense(6, input_shape=(6,), kernel_initializer='normal', activation='relu'))
model.add(Dense(6,  kernel_initializer='normal', activation='relu'))
model.add(Dense(6,  kernel_initializer='normal', activation='relu'))
model.add(Dense(1,kernel_initializer='normal'))
model.summary()

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

model.fit(X_train.values, y_train.values, epochs=25, batch_size=50,  verbose=1)

y_pred=model.predict(X_test.values)


RMSE_overall = np.sqrt(mean_squared_error(y_test.values, y_pred))
print(RMSE_overall)

model_test = pd.read_csv("model_test.csv")
model_test = model_test.fillna(model_test.mean())
model_test = model_test.iloc[:,1:]

model_test.loc[((model_test.iloc[:,6]==0) & (model_test.iloc[:,1]==0) & (model_test.iloc[:,2]==0)),'2'] = 0.82
model_test.loc[((model_test.iloc[:,6]==0) & (model_test.iloc[:,1]==0)) ,'6'] = 0.85

X_test = model_test.iloc[:,1:]

pd.DataFrame(model.predict(X_test.values)).to_csv("Overall.csv",header=False,index=False)
