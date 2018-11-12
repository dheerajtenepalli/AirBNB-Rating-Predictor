#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the main model used to predict the ratings for Overall rating and several other sub categories.
"""

"""
Created on Fri Jul 27 01:38:02 2018

@author: reddy
"""

import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = pd.read_csv("model_train_version_3.csv")
X = X.iloc[:,1:]
X = X[(X.iloc[:,116]!=0) & (X.iloc[:,112]!=0)]
X = X.fillna(X.mean())
X =X.drop('17',axis=1)

#Model for Predicting Overall rating
Overall_rating_X = X.iloc[:,:116]
Overall_rating_X  = Overall_rating_X.drop(Overall_rating_X.columns[109],axis=1)
Overall_rating_y = X.iloc[:,116]
X_train, X_test, y_train, y_test = train_test_split(Overall_rating_X, Overall_rating_y, test_size=0.0, random_state=48)

#Recursive feature elimination
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
rfe = RFE(model, 10)
rfe = rfe.fit(X_train, y_train)
feat_names = X_train.columns
rfe_result = pd.DataFrame({'feature': feat_names, 'ranking': rfe.ranking_, 'selection': rfe.support_})
rfe_result.sort_values(by='ranking')[:10]

regr_overall = RandomForestRegressor(n_estimators=400,max_features = 0.8
                                    ,max_depth = 50)
regr_overall.fit(X_train.values, y_train.values)
y_pred = regr_overall.predict(X_test)
RMSE_overall = np.sqrt(mean_squared_error(y_test.values, y_pred))

#Model for Predicting accuracy rating
accuracy_X = X.iloc[:,:116]
accuracy_X  = accuracy_X.drop(accuracy_X.columns[109],axis=1)
accuracy_y = X.iloc[:,117]
X_train_acc, X_test_acc, y_train_acc, y_test_acc = train_test_split(accuracy_X, accuracy_y, test_size=0.0, random_state=42)
regr_acc = RandomForestRegressor(n_estimators=400,max_depth=50,max_features = 0.8)
regr_acc.fit(X_train_acc, y_train_acc)

#Model for Predicting Cleanliness rating
accuracy_X_2 = X.iloc[:,:116]
accuracy_X_2 = accuracy_X_2.drop(accuracy_X_2.columns[109],axis=1)
accuracy_y_2 = X.iloc[:,118]
X_train_acc_2, X_test_acc_2, y_train_acc_2, y_test_acc_2 = train_test_split(accuracy_X_2, accuracy_y_2, test_size=0.2, random_state=42)
regr_acc_2 = RandomForestRegressor(n_estimators=200,max_depth=9,max_features = 0.8)
regr_acc_2.fit(X_train_acc_2, y_train_acc_2)
y_pred_acc_2 = regr_acc_2.predict(X_test_acc_2)
RMSE_2 = np.sqrt(mean_squared_error(y_test_acc_2.values, y_pred_acc_2))
