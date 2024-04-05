import pandas as pd

df=pd.read_json('/workspaces/Random-Python-Work/2024/March/RandomValuesGenerations/stock_by_key/ANVS.json',lines=True)

print(df.head())