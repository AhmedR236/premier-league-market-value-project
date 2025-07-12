import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
