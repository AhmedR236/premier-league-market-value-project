import pandas as pd

# Kaggle dataset For 23/24 Market Values: https://www.kaggle.com/datasets/davidcariboo/player-scores/data?select=clubs.csv

df1 = pd.read_csv('data/clubs.csv') #GB1 is premier league in the dataset 
df2 = pd.read_csv('data/players.csv')
df3 = pd.read_csv('data/player_valuations.csv')

#df1 = print(df1.columns)

df1 = df1[df1['domestic_competition_id'] == 'GB1'] #Retrieving only Premier League clubs
df1['last_season'] = df1['last_season'].astype(int) #Making sure last season is an int
df1['club_id'] = df1['club_id'].astype(int) #Making sure club_id is an int
#print(df1.dtypes)

df1.drop(['club_code', 'total_market_value', 'squad_size', 'average_age', 'foreigners_number', 'foreigners_percentage', 
          'national_team_players', 'stadium_name', 'stadium_seats', 'net_transfer_record', 'coach_name', 'filename', 'url'], axis=1, inplace=True) #unnecessary columns

df1 = df1[df1['last_season'] >= 2023] #Filtering clubs that were in the Premier League in 23/24
df1 = df1[df1['last_season'] <= 2024] #Filtering clubs that were in the Premier League in 23/24

df1 = df1[df1['name'] != 'Leicester City Football Club'] #Removing Leicester City as they were promoted in 2024
df1 = df1[df1['name'] != 'Southampton Football Club'] #Removing Southampton as they were promoted in 2024
df1 = df1[df1['name'] != 'Ipswich Town Football Club'] #Removing Ipswich Town as they were promoted in 2024

df1['name'] = df1['name'].str.replace('Football Club', '', regex=False) #Removing 'Football Club' from club names
df1['name'] = df1['name'].str.replace('FC', '', regex=False) #Removing 'FC' from club names
df1['name'] = df1['name'].str.replace('Association', '', regex=False) #Removing Association
df1['name'] = df1['name'].str.replace('Hotspur', '', regex=False) #Removing Hotspur
df1['name'] = df1['name'].str.replace('and Hove Albion', '', regex=False) #Removing Brighton's wonky name

#print(df1)
#print(f'Count: {len(df1)}')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#print(df2.columns)

df2.drop(['first_name', 'last_name', 'player_code', 'country_of_birth', 'city_of_birth', 'country_of_citizenship', 'date_of_birth', 'sub_position', 'position', 
           'foot', 'height_in_cm', 'contract_expiration_date', 'agent_name', 'image_url', 'url', 'highest_market_value_in_eur', 'market_value_in_eur', 'current_club_name'], axis=1, inplace=True) #unnecessary columns

df2 = df2[df2['current_club_domestic_competition_id'] == 'GB1'] #Filtering players that are in the Premier League
df2 = df2[df2['last_season'] >= 2023] #Filtering clubs that were in the Premier League in 23/24
df2 = df2[df2['last_season'] <= 2024] #Filtering clubs that were in the Premier League in 23/24
#print(df2)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

df3 = df3[df3['date'] >= '2023-08-01'] #Filtering player valuations from 1st August 2023
df3 = df3[df3['date'] <= '2024-06-30'] #Filtering player valuations until 30th June 2024

df3 = df3[df3['player_club_domestic_competition_id'] == 'GB1'] #Filtering players that are in the Premier League
#print(df3)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

merged_df = pd.merge(df1, df2, left_on='club_id', right_on='current_club_id') #Merging clubs
merged_df['CLUB_ID'] = merged_df['club_id'] #New col for club_id
merged_df = merged_df.rename(columns={'name_x': 'CLUB'}) #Renaming
merged_df = merged_df.rename(columns={'name_y': 'PLAYER'}) #Renaming
merged_df = merged_df.drop(['club_id', 'current_club_id', 'current_club_domestic_competition_id', 
                            'last_season_y', 'last_season_x'], axis=1)

df = pd.merge(merged_df, df3, left_on='player_id', right_on='player_id') #Merging player valuations
#print(df.columns)

df = df.drop(['domestic_competition_id', 'player_id', 'CLUB_ID', 'date', 'current_club_id', 'player_club_domestic_competition_id'], axis=1)
#print(df.columns)

df = df.rename(columns={'market_value_in_eur': 'Market Value (EUROS)'}) #Renaming
df = df.drop_duplicates(subset='PLAYER')  # Remove duplicate players
#print(df)

df.to_csv('data/cleaned_MV_23_24.csv', index = False, encoding='utf-8-sig')