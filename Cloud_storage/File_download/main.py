from google.cloud import storage

service_account = "" # credentials, ie .json file

bucket_name = ""
bucket_file_path = ""
file_name = ""
blob_name = bucket_file_path + file_name

storage_client = storage.Client.from_service_account_json(service_account)
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.download_to_filename(file_name)

print(f"{file_name} downloaded from {bucket_name}/{bucket_file_path}")
