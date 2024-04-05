import pandas as pd
import os
import pytz

df=pd.read_json('/workspaces/Random-Python-Work/2024/March/RandomValuesGenerations/stock_by_key/ANVS.json',lines=True)
df['end_timestamp'] = pd.to_datetime(df['end_timestamp'], unit='ms',utc=True).dt.tz_convert('US/Eastern')
print(df['event_type'].count())
print(df['volume'].sum())
print(df['end_timestamp'].max())
print()
print(df.columns)
