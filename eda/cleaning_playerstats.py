import soccerdata
from soccerdata import FBref

#python3 -m pip install soccerdata

fbref = FBref(leagues="ENG-Premier League", seasons="2023-2024")
fbref2 = FBref(leagues="ENG-Premier League", seasons="2024-2025")

df = fbref.read_player_season_stats(stat_type="standard") #23/24
df2 = fbref2.read_player_season_stats(stat_type="standard") #24/25


# Filtering out players who played less than 60 min per match. (38 games * 60 min = 2280 min)
dfclean = df[df['Playing Time', 'Min'] >= 2280]
df2clean = df2[df2['Playing Time', 'Min'] >= 2280]

dfclean.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in dfclean.columns] #Flattening Column Names so it is in a format like Performance_Gls
df2clean.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df2clean.columns]


dfclean.to_csv('cleaned23_24.csv', index = 'false', encoding='utf-8-sig')
df2clean.to_csv('cleaned24_25.csv', index = 'false', encoding='utf-8-sig')


