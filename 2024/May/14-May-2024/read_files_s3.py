import pandas as pd
import boto3

def read_files_s3_bucket(bucket_name, folder_name):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
    file_list = []
    for obj in response['Contents']:  
        file_list.append(obj['Key'])
        
    dataset =pd.DataFrame()
    for x in range(1,len(file_list)):
        temp_df = pd.read_json('s3://airflowprojects/'+file_list[x],lines=True)
        dataset = pd.concat([dataset,temp_df])
    return dataset

if __name__ == "__main__":
    data = read_files_s3_bucket('bucketname','folder_name/')
    print(data.shape)
