import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.metrics import root_mean_squared_error, mean_squared_error, r2_score
import joblib

# Ran it in venv in cmd 
# python src/24_25_train.py

model = joblib.load('models/xgb_23_24_model.pkl')

features = [
    "age_",
    "pos_",
    "team",
    "Performance_Gls",
    "Performance_G+A",
    "Per 90 Minutes_Gls",
    "Per 90 Minutes_G+A",
    "Performance_G-PK",
    "Per 90 Minutes_G+A-PK",
    "Per 90 Minutes_G-PK",
    "Per 90 Minutes_xG+xAG",
    "Expected_npxG+xAG",
    "Expected_xG",
    "Expected_npxG",
    "Per 90 Minutes_xG",
    "Per 90 Minutes_npxG",
    "Progression_PrgP",
    "Performance_Ast",
    "Per 90 Minutes_Ast",
    "Expected_xAG",
    "Performance_PKatt"
]  


df2 = pd.read_csv('data/official_24_25.csv')
df2 = df2[df2['MARKET VALUE (EUROS)'] < 100000000] # Filtering out players with market value over 100 million euros, as they are outliers and making model worse

x2 = df2[features]
x2 = pd.get_dummies(df2, columns=['team','pos_']) 


#This is a try and catch method to ensure the feature names are consistent amongst both sets
try:                                            
    feature_cols = model.feature_names_in_
except AttributeError:
    feature_cols = model.get_booster().feature_names

x2 = x2.reindex(columns = feature_cols, fill_value = 0)

y2 = df2['MARKET VALUE (EUROS)'].astype(int) #Target variable and ensuring its an int

y2_pred = model.predict(x2)
rmse = root_mean_squared_error(y2, y2_pred) 
r2 = r2_score(y2, y2_pred)
scores = cross_val_score(model, x2, y2, cv=5, scoring='r2') #Ensuring the model is not overfitting by cross-validation

print(f'Root Mean Squared Error: {rmse}') 
print(f'R^2 Test: {r2}')
print(f'Average R^2: {scores.mean()}')

#Root Mean Squared Error: 14940793.0   #This testing is not actually bad since this season had a lot of unexpected twists to huge teams. Such as underperformance, and large number of injuries
#R^2 Test: 0.4724881052970886
#Average R^2: 0.4245340943336487   