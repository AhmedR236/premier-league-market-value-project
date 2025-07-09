import pandas as pd

df = pd.read_csv('data/RAW_premier-player-23-24.csv', index_col=0)
print(df.head())

#Remove duplicates 
df = df.drop_duplicates(subset=['Player'])

# Filtering out players who played less than 60 min per match. (38 games * 60 min = 2280 min)
df = df.query('Min >= 2280')

