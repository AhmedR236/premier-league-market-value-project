import pandas as pd 
import joblib
from xgboost import XGBRegressor

df = pd.read_csv('data/official_24_25.csv')
df = df[df['MARKET VALUE (EUROS)'] < 100000000] # Filtering out players with market value over 100 million euros, as they are outliers and making model worse

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

x = df[features]
x = pd.get_dummies(x, columns=['team','pos_']) 
y = df['MARKET VALUE (EUROS)'].astype(int) 

xgb_model = XGBRegressor (  
objective='reg:squarederror', 
n_estimators = 120, # Number of trees in the ensemble, set to 120 so I dont overfit
learning_rate = 0.1, 
max_depth = 2 # If I make the tree deeper it will overfit
)

xgb_model.fit(x, y) 
joblib.dump(xgb_model, 'models/xgb_25_26_model.pkl') #Saving the 25_26 model for when the 25_26 season ends to identify mvs with those metrics 

# Ran it in venv in cmd 
# python src/25_26_model.py
