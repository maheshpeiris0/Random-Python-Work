import os
import pandas as pd
import pytz
import boto3
from botocore.exceptions import ClientError
import gspread
import json
import time

def google_sheet_return_updated(folder_path):
    sub_folders_name=['return_5%', 'return_10%','return_20%','return_more_20%','other','return_5%_1','return_10%_1','return_20%_1','return_more_20%_1']
    final_list=[]
    for folder in sub_folders_name:
        try:
            full_folder_path = os.path.join(folder_path, folder)
            full_file_paths = [os.path.join(full_folder_path, f) for f in os.listdir(full_folder_path) if os.path.isfile(os.path.join(full_folder_path, f))]
            for file in full_file_paths:
                df=pd.read_json(file,lines=True)
                df['end_timestamp'] = pd.to_datetime(df['end_timestamp'], unit='ms',utc=True).dt.tz_convert('US/Eastern')
                df.sort_values(by='end_timestamp',ascending=True,inplace=True)
                price_return = (df['close'].iloc[-1] - df['close'].iloc[0])/df['close'].iloc[0]
                dict ={'Symbol':df['symbol'].iloc[0],'Return':price_return,'Close':df['close'].iloc[-1],'Count':df.shape[0],'Total_Volumne':df['volume'].sum(),'AVG_Volume':df['volume'].mean(),'Open':df['open'].min(),'High':df['high'].max(),'Folder':folder,'last_updated':df['end_timestamp'].iloc[-1].strftime('%Y-%m-%d %H:%M:%S')}
                final_list.append(dict)
        except FileNotFoundError:
            print(f"File Not Found {folder}")
            continue
        except OSError as e:
            print(f"Error: {e}")
            continue
    final_df = pd.DataFrame(final_list)
    secret_name = "secret_name"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        print(e)
        exit()

    secret = get_secret_value_response['SecretString']
    key_data = json.loads(secret)
    gc = gspread.service_account_from_dict(key_data)
    sht1 = gc.open_by_key('sheet_id')
    worksheet = sht1.worksheet("Returns") #sheet name
    worksheet.clear()
    worksheet.update([final_df.columns.values.tolist()] + final_df.values.tolist())
    


if __name__ == "__main__":
    folder_path = "/home/ec2-user/project/stock_by_key"
    while True:
        google_sheet_return_updated(folder_path)
        time.sleep(30)
    
