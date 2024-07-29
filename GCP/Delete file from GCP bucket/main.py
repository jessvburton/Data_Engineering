from google.cloud import storage

service_account = "prodSA.json"

bucket_name = ""
bucket_file_path = ""
file_name = ""
blob_name = bucket_file_path + file_name

storage_client = storage.Client.from_service_account_json(service_account)
bucket = storage_client.bucket(bucket_name)

# single object in the directory
blob = bucket.blob(blob_name)
blob.delete()
print(f"{blob} deleted from {bucket_name}/{bucket_file_path}")

# # all objects in the directory
# blobs = bucket.list_blobs(prefix=bucket_file_path)
# for blob in blobs:
#     blob.delete()
#     print(f"{blob} deleted from {bucket_name}/{bucket_file_path}")
