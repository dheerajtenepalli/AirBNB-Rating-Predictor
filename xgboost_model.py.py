import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.ensemble import RandomForestRegressor


X = pd.read_csv("model_train.csv")
X = X.iloc[:,1:]
X = X[(X.iloc[:,6]!=0) & (X.iloc[:,1]!=0)]
X = X.fillna(X.mean())

#Droppping Listing_id
X = X.iloc[:,1:]
from sklearn.model_selection import train_test_split



Overall_rating_X = X.iloc[:,:7]
Overall_rating_y = Overall_rating_X.iloc[:,6]
Overall_rating_X = Overall_rating_X.iloc[:,:-1]
X_train, X_test, y_train, y_test = train_test_split(Overall_rating_X, Overall_rating_y, test_size=0.2, random_state=48)
from xgboost import XGBRegressor
regr_overall = XGBRegressor(n_estimators=200,max_depth=10,eval_metric = 'rmse',booster = 
'dart')
regr_overall.fit(X_train, y_train)
print("Done with Fitting")
y_pred = regr_overall.predict(X_test)

RMSE_overall = np.sqrt(mean_squared_error(y_test.values, y_pred))
print(RMSE_overall)
