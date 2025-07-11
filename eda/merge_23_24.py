import pandas as pd

df1 = pd.read_csv('data/cleaned23_24.csv')
df2 = pd.read_csv('data/cleaned_MV_23_24.csv')

df1['team'] = df1['team'].str.strip().str.lower()
df2['CLUB'] = df2['CLUB'].str.strip().str.lower()

df1['player'] = df1['player'].str.strip().str.lower()
df2['PLAYER'] = df2['PLAYER'].str.strip().str.lower()


df = pd.merge(df1, df2, left_on=['team', 'player'], right_on=['CLUB', 'PLAYER'], how='left')
df = df.drop(['CLUB', 'PLAYER'], axis=1)  

#df.to_csv('data/RAW_merged_23_24.csv', index=False, encoding='utf-8-sig')

################################################################################################################################
#Some players didnt get merged due to name inconsistencies, so I merged them manually and saved it in official_merged_23_24.csv
################################################################################################################################
