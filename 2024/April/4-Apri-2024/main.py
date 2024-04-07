import pandas as pd
import os
import pytz

df=pd.read_json('/workspaces/Random-Python-Work/2024/March/RandomValuesGenerations/stock_by_key/return_10%/ANVS.json',lines=True)
df['end_timestamp'] = pd.to_datetime(df['end_timestamp'], unit='ms',utc=True).dt.tz_convert('US/Eastern')
df.sort_values(by='end_timestamp',ascending=True,inplace=True)
price_return = (df['close'].iloc[-1] - df['close'].iloc[0])/df['close'].iloc[0]
dict ={'Symbol':df['symbol'].iloc[0],'Return':price_return,'Close':df['close'].iloc[-1],'Count':df.shape[0],'Total_Volumne':df['volume'].sum(),'AVG_Volume':df['volume'].mean(),'Open':df['open'].min(),'High':df['high'].max()}
#print(dict)


file_path = '/workspaces/Random-Python-Work/2024/March/RandomValuesGenerations/stock_by_key'
print(os.listdir(file_path))

inner_folder =['return_5%', 'return_10%', 'other']


final_list =[]
for folder in inner_folder:
    full_folder_path = os.path.join(file_path, folder)
    full_file_paths = [os.path.join(full_folder_path, f) for f in os.listdir(full_folder_path) if os.path.isfile(os.path.join(full_folder_path, f))]
    for file in full_file_paths:
        df=pd.read_json(file,lines=True)
        df['end_timestamp'] = pd.to_datetime(df['end_timestamp'], unit='ms',utc=True).dt.tz_convert('US/Eastern')
        df.sort_values(by='end_timestamp',ascending=True,inplace=True)
        price_return = (df['close'].iloc[-1] - df['close'].iloc[0])/df['close'].iloc[0]
        dict ={'Symbol':df['symbol'].iloc[0],'Return':price_return,'Close':df['close'].iloc[-1],'Count':df.shape[0],'Total_Volumne':df['volume'].sum(),'AVG_Volume':df['volume'].mean(),'Open':df['open'].min(),'High':df['high'].max()}
        #dataset =pd.DataFrame(dict)
        final_list.append(dict)
    #final_df=pd.concat([final_df,dataset],axis=0)


final_df = pd.DataFrame(final_list)
print(final_df)