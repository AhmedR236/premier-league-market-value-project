import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import root_mean_squared_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib

# Ran it in venv in cmd 
# python src/23_24_model.py

df = pd.read_csv('data/official_23_24.csv')
df = df[df['Market Value (EUROS)'] < 100000000] # Filtering out players with market value over 100 million euros, as they are outliers and making model worse

x = df.copy() # Create a copy of the original DataFrame

#Relevant attributes for the model
features = [
    "age_",
    "team",
    "pos_",
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

x = x[features] # Selecting relevant features

x = pd.get_dummies(x, columns = ['team', 'pos_']) #Transforming categorical variables into ints for training
y = df['Market Value (EUROS)'].astype(int) #Target variable and ensuring its an int

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=43) #Train-test split. Testing on 20% of the data

#XGBoost model
xgb_model = XGBRegressor (  
objective='reg:squarederror', 
n_estimators = 120, # Number of trees in the ensemble, set to 120 so I dont overfit
learning_rate = 0.1, 
max_depth = 2 # If I make the tree deeper it will overfit
)

xgb_model.fit(x_train, y_train) #Fitting the model

joblib.dump(xgb_model, 'models/xgb_23_24_model.pkl') #Saving the model to use on 24_25 data

y_pred = xgb_model.predict(x_test) #Making predictions on the target variable

#Model Evaluation
rmse = root_mean_squared_error(y_test, y_pred)  #Calculating Root Mean Squared Error
r2_train = xgb_model.score(x_train, y_train)  #Calculating R^2 score for training data
r2_test = r2_score(y_test, y_pred)  #Calculating R^2 score
scores = cross_val_score(xgb_model, x, y, cv=5, scoring='r2') #Ensuring the model is not overfitting by cross-validation
df_results = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred}) #Creating a df to store the pred vs actual values

print(f'Root Mean Squared Error: {rmse}')
print(f'R^2 (Train): {r2_train}')  
print(f'R^2 (Test): {r2_test}')  
print("Average R^2:", scores.mean())
print("\nActual vs. Predicted Market Values (first 10):")
print(df_results.head(10).to_string(index=False))


#Root Mean Squared Error: 14572454.0   #The best results I got
#R^2 (Train): 0.9236470460891724
#R^2 (Test): 0.6897004246711731
#Average R^2: 0.5310466885566711

##################################################################

#Plotting Actual vs Predicted Values 

plt.figure(figsize=(12, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='blue', label ='Predicted Values')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Actual')
plt.title('Actual vs Predicted Market Value')
plt.xlabel('Actual Market Value (Millions of Euros)')
plt.ylabel('Predicted Market Value (Millions of Euros)')
plt.legend()
plt.grid(True)
plt.show()



