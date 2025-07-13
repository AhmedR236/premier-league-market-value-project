import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/official_24_25.csv")

numbersonly = df.select_dtypes(include=['int64', 'float64']) #Used to only select columns that have numbers in them (getting rid of name, club etc.)

correlation = numbersonly.corr() #(Correlation Matrix) Computes all possible combinations

plt.figure(figsize=(20,10))
sns.heatmap(correlation[['MARKET VALUE (EUROS)']].sort_values(by='MARKET VALUE (EUROS)', ascending=False), annot=True, cmap='coolwarm') #Heatmap displays it to 'Market Value (EUROS)
plt.title('Correlation Factor to Market Value')
plt.show()

df['Market Value (Millions)'] = df['MARKET VALUE (EUROS)'] / 1_000_000

plt.figure(figsize=(12, 6))
plt.scatter(df['Performance_G+A'], df['Market Value (Millions)'])
plt.title('Market Value (in Millions) vs Performance_G+A')
plt.xlabel('Performance_G+A')
plt.ylabel('Market Value (Millions of Euros)')
plt.grid(False)
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(df['Performance_Gls'], df['Market Value (Millions)'])
plt.title('Market Value (in Millions) vs Goals')
plt.xlabel('Goals')
plt.ylabel('Market Value (Millions of Euros)')
plt.grid(False)
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(df['Per 90 Minutes_Gls'], df['Market Value (Millions)'])
plt.title('Market Value (in Millions) vs Goals Per 90')
plt.xlabel('Goals per 90')
plt.ylabel('Market Value (Millions of Euros)')
plt.grid(False)
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(df['age_'], df['Market Value (Millions)'])
plt.title('Market Value (in Millions) vs Age')
plt.xlabel('Age')
plt.ylabel('Market Value (Millions of Euros)')
plt.grid(False)
plt.show()

########################################################################################################################

#Feature Engineering (Binning Age Groups To Identify Ranges of Impact on Market Value)

df['Age Group'] = pd.cut(df['age_'], bins=[0, 20, 25, 30, 35, 40, 100], labels=['<20', '20-25', '25-30', '30-35', '35-40', '>40']) #Creating Age Groups

plt.figure(figsize=(10,6))
sns.barplot(x='Age Group', y='Market Value (Millions)', data=df, estimator=np.mean, errorbar=None)
plt.title('Average Market Value by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Market Value (Millions of Euros)')
plt.show() # Ages from 20-25 has the highest average market value. 
#This implies that players in their early to mid-20s tend to have the highest market values, likely due to a combination of potential and performance.


#Feature Engineering (Based on teams and Market Value)

plt.figure(figsize=(12,6))
sns.barplot(x='team', y='Market Value (Millions)', data=df, estimator=np.mean, errorbar=None) 
plt.title('Average Market Value by Team')
plt.xlabel('Team')
plt.ylabel('Average Market Value (Millions of Euros)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show() #5/6 Big 6 teams have the highest average market value, which is expected due to their financial power. (Man City, Arsenal, Liverpool, Chelsea, Tottenham Hotspur)
#So the market value of players has a slight influence based on the team they play for. This isnt a primary factor for market value, but it does slightly influence the players value.


#Feature Engineering Market Value Based on Positions

p = df['pos_'].unique()
#print(p)

#['GK' 'MF' 'DF' 'FW,MF' 'FW' 'MF,DF' 'DF,FW' 'MF,FW'] unique positions in the dataset

plt.figure(figsize=(10,6))
sns.barplot(x='pos_', y='Market Value (Millions)', data=df, estimator=np.mean, errorbar=None)
plt.title('Average Market Value by Position')
plt.xlabel('Position')
plt.ylabel('Average Market Value (Millions of Euros)')
plt.show() 
#Forwards have the highest average market value, followed by midfielders, defenders, and goalkeepers. Which makes sense.
