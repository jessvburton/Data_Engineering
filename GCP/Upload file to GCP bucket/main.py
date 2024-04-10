import os.path
import pandas as pd
from google.cloud import storage

service_account = "" # file with credentials

file_path = '' # file name you want to upload
file_name = os.path.basename(file_path)
file = pd.read_csv(file_path)

bucket_name = "" # bucket name you want to upload to
bucket_file_path = f"" # bucket filepath and file name

storage_client = storage.Client.from_service_account_json(service_account)
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(bucket_file_path)
blob.upload_from_string(file.to_csv(index=False), content_type='text/csv')

print(f"{file_name} uploaded to {bucket_name}/{bucket_file_path}")
