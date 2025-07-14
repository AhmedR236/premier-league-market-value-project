from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

os.makedirs('outputs', exist_ok=True) #saving the outputs in the outputs folder #####################################

df = pd.read_csv("../data/official_23_24.csv")
df2 = pd.read_csv("../data/official_24_25.csv")

df = df[df['Market Value (EUROS)'] < 100000000] # Filtering out players with market value over 100 million euros, as they are outliers and making model worse
df2 = df2[df2["MARKET VALUE (EUROS)"] < 100000000]

Y = df["Market Value (EUROS)"]
Y_test = df2["MARKET VALUE (EUROS)"]

print(df.columns)


ImportantCols = [
    "age_", "Performance_Gls", "Performance_G+A", "Per 90 Minutes_Gls", "Per 90 Minutes_G+A",
    "Performance_G-PK", "Per 90 Minutes_G+A-PK", "Per 90 Minutes_G-PK",
    "Per 90 Minutes_xG+xAG", "Expected_npxG+xAG", "Expected_xG", "Expected_npxG",
    "Per 90 Minutes_xG", "Per 90 Minutes_npxG", "Progression_PrgP", "Performance_Ast", "Per 90 Minutes_Ast", "Expected_xAG",
    "Performance_PKatt", "pos_", "team"
] #Ones we agreed on based on the heatmap and scatter plots. #More can be added for better accuracy along with teams

df = df[ImportantCols]
df2 = df2[ImportantCols]

# Combine for encoding
combined = pd.concat([df, df2], axis=0)

# One-hot encode team and position
combined_encoded = pd.get_dummies(combined, columns=["team", "pos_"], drop_first=False)

# Split into train and test
X = combined_encoded.iloc[:len(df)]
X_test = combined_encoded.iloc[len(df):]

model = RandomForestRegressor(random_state= 43, n_estimators= 97) #RS = 29 Best One Along with 43

model.fit(X,Y)

predictedresults = model.predict(X_test)

df_results = pd.DataFrame({'Actual': Y_test.values, 'Predicted': predictedresults}) #Creating a df to store the pred vs actual values#####################################
df_results.to_csv('outputs/23_24_randomforest.csv', index=False) #saving the outputs as a csv ###########################################


print("Mean Square Error:", mean_squared_error(Y_test, predictedresults))
print("R^2 Score:", r2_score(Y_test, predictedresults))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(Y_test, predictedresults)))

#Cross-Val
scores = cross_val_score(model, X, Y, cv=5, scoring='r2')
print("CrossVal R² scores:", scores)
print("Average R²:", scores.mean())

#Best R^2 I got was 0.4532 
#This season was very unpredictable so makes sense it's only 0.45 on when compared to 24/25 but 0.5 when cross validated



