from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as py
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("data/official_23_24.csv")
df2 = pd.read_csv("data/official_24_25.csv")
Y = df["Market Value (EUROS)"]
Y_test = df2["MARKET VALUE (EUROS)"]

print(df.columns)

ImportantCols = [
    "age_", "Performance_Gls", "Expected_npxG", "Expected_npxG+xAG", "Performance_G+A"
]

df = df[ImportantCols]
df2 = df2[ImportantCols]

X = df
X_test = df2

print(X.isnull().sum())
print(X_test.isnull().sum())

model = RandomForestRegressor(random_state= 15) #What The Flip is a 42

model.fit(X,Y)

predictedresults = model.predict(X_test)

print("Mean Square Error:", mean_squared_error(Y_test, predictedresults))
print("R^2 Score:", r2_score(Y_test, predictedresults))





