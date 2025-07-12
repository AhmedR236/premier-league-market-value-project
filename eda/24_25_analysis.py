import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

#python eda/24_25_analysis.py

df = pd.read_csv('data/official_24_25.csv')

df = df.rename(columns={'Market  Value (EUROS)': 'MARKET VALUE (EUROS)'})

df['MARKET VALUE (EUROS)'] = df['MARKET VALUE (EUROS)'].astype(int) 

#print(df.dtypes) 

#df.to_csv('data/official_24_25.csv', index=False, encoding='utf-8-sig')

# Had a minor inconsistency issue and had to fix it 
#######################################################################################################

#Analysis


