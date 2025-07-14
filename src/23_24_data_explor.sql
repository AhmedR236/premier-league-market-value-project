-- These statements are from MySQL--------------
-- The outputs were in MyS
CREATE TABLE raw_merged_23_24_filtersql (
  league VARCHAR(50),
  season INT,		  
  team  VARCHAR(50),
  player VARCHAR(50),
  pos_  VARCHAR(30),
  age_  INT);

--Loading in the data for these cols
LOAD DATA LOCAL INFILE 'C:/Users/Ahmed/OneDrive/Desktop/Projects/CS Projects/Prem Project/premier-league-market-value-forecasting-project/data/RAW_merged_23_24.csv'
INTO TABLE raw_merged_23_24_filtersql
FIELDS TERMINATED BY ',' 
(league, season, team, player, pos_, age_); 


SELECT player, COUNT(*) AS count --Getting count of each player to ensure there isnt any duplicates
FROM raw_merged_23_24_filtersql
GROUP BY player
HAVING count > 1;

SELECT
  SUM(player IS NULL) AS player_null, --Making sure these key attributes are not NULL since they are strings 
  SUM(team IS NULL) AS team_null,
  SUM(pos_ IS NULL) AS pos_null,
FROM raw_merged_23_24_filtersql;