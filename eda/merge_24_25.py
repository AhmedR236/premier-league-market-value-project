import pandas as pd

df1 = pd.read_csv('data/cleaned24_25.csv')
df2 = pd.read_csv('data/24_25_MV.csv')

df1['player'] = df1['player'].str.strip().str.lower()
df2['Player Name'] = df2['Player Name'].str.strip().str.lower()


df = pd.merge(df1, df2, left_on=['player'], right_on=['Player Name'], how='left')
df = df.drop(['Nationality', 'Position', 'Age'], axis=1)
df = df.drop_duplicates(subset=['player'])

def convert_market_value(val):
    if pd.isna(val):
        return None
    val = str(val).replace('€', '').replace('m', '').replace(',', '').strip()
    try:
        return int(float(val) * 1_000_000)
    except ValueError:
        return None

df['Market Value'] = df['Market Value'].apply(convert_market_value)

df.to_csv('data/RAW_merged_24_25.csv', index=False, encoding='utf-8-sig')

############################################################################################################################################################
#Some players didnt get merged due to name inconsistencies, so I corrected the inconsistencies and merged them manually and saved it in official_24_25.csv
############################################################################################################################################################
