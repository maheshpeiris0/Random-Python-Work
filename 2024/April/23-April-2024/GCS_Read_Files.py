def read_files_GCS(bucket_name,folder_name,file_saved_path):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_name, delimiter='/')
    files_names = [blob.name for blob in blobs]
    for file in files_names:
        full_file_path = f'gs://{bucket_name}/{file}'
        dataset = pd.read_parquet(full_file_path)
        merge_data = pd.concat([merge_data, dataset], axis=0)
    merge_data.to_parquet(file_saved_path)
    return merge_data
