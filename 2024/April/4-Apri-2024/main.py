import pandas as pd
import os
import pytz

df=pd.read_json('/workspaces/Random-Python-Work/2024/March/RandomValuesGenerations/stock_by_key/ANVS.json',lines=True)
df['end_timestamp'] = pd.to_datetime(df['end_timestamp'], unit='ms',utc=True).dt.tz_convert('US/Eastern')
df.sort_values(by='end_timestamp',ascending=True,inplace=True)
price_return = (df['close'].iloc[-1] - df['close'].iloc[0])/df['close'].iloc[0]
dict ={'Count':df.shape[0],'Total_Volumne':df['volume'].sum(),'Open':df['open'].min()}

print(df['event_type'].count())
print(df['volume'].sum())
print(df['end_timestamp'].max())
print(df['open'].min())

print(df['close'].max())
print(df['high'].max())

print(df['close'].max())
print(df['close'].idxmax())
print(df['close'].iloc[-1])
print(df.tail(1))