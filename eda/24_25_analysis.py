import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

#python eda/24_25_analysis.py

df = pd.read_csv('data/official_24_25.csv')

df = df.rename(columns={'Market  Value (EUROS)': 'MARKET VALUE (EUROS)'})
def convert_market_value(val):
    if pd.isna(val):
        return None
    val = str(val).replace('€', '').replace('m', '').replace(',', '').strip()
    try:
        return int(float(val) * 1_000_000)
    except ValueError:
        return None

df['MARKET VALUE (EUROS)'] = df['MARKET VALUE (EUROS)'].apply(convert_market_value)

df['MARKET VALUE (EUROS)'] = df['MARKET VALUE (EUROS)'].astype(int) 

print(df.dtypes) 

df.to_csv('data/official_24_25.csv', index=False, encoding='utf-8-sig')

