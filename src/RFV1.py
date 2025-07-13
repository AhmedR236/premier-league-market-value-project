from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("../data/official_23_24.csv")
df2 = pd.read_csv("../data/official_24_25.csv")
Y = df["Market Value (EUROS)"]
Y_test = df2["MARKET VALUE (EUROS)"]

print(df.columns)

ImportantCols = [
    "age_",  "Performance_Gls", "Performance_G+A", "Per 90 Minutes_Gls", "Per 90 Minutes_G+A",
    "Performance_G-PK", "Per 90 Minutes_G+A-PK", "Per 90 Minutes_G-PK",
    "Per 90 Minutes_xG+xAG", "Expected_npxG+xAG", "Expected_xG", "Expected_npxG",
    "Per 90 Minutes_xG", "Per 90 Minutes_npxG", "Progression_PrgP", "Performance_Ast", "Per 90 Minutes_Ast", "Expected_xAG",
    "Performance_PKatt", 
] #Ones we agreed on based on the heatmap and scatter plots. #More can be added for better accuracy along with teams

df = df[ImportantCols]
df2 = df2[ImportantCols]

X = df
X_test = df2

print(X.isnull().sum())
print(X_test.isnull().sum())

model = RandomForestRegressor(random_state= 15)

model.fit(X,Y)

predictedresults = model.predict(X_test)

print("Mean Square Error:", mean_squared_error(Y_test, predictedresults))
print("R^2 Score:", r2_score(Y_test, predictedresults))

rmse = np.sqrt(mean_squared_error(Y_test, predictedresults))
print("Root Mean Squared Error:", rmse)

#Best R^2 I got was 0.4326 and Best MeanSquare Error: 419429118370746.25



