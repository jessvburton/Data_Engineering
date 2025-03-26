# Google Cloud Storage CSV Upload Script

This script demonstrates how to upload a CSV file (read using pandas) to a Google Cloud Storage (GCS) bucket using the `google-cloud-storage` and `pandas` Python libraries.

## Prerequisites

1.  **Google Cloud Platform (GCP) Account:** You need an active GCP account.
2.  **Google Cloud Storage Bucket:** You need an existing GCS bucket where you want to upload the file.
3.  **Service Account JSON Key:** You need a service account JSON key file with appropriate permissions to write objects in the bucket.
4.  **Python 3.x:** Ensure you have Python 3.x installed.
5.  **`google-cloud-storage` and `pandas` Libraries:** Install the libraries using pip:

    ```bash
    pip install google-cloud-storage pandas
    ```

## Setup

1.  **Service Account Key:**
    * Download your service account JSON key file.
    * Modify the `service_account` variable in the script to point to the path of your JSON key file. For example if the file is called `my-service-account.json` the variable should be set to `service_account = "my-service-account.json"`
    * **Important:** Ensure this service account has the `storage.objects.create` permission on the target bucket.
2.  **Configuration:**
    * Open the Python script and modify the following variables:
        * `service_account`: Path to your service account JSON key file (e.g., `"my-service-account.json"`).
        * `file_path`: Path to the local CSV file you want to upload.
        * `bucket_name`: Name of your GCS bucket.
        * `bucket_file_path`: Path and filename within the bucket where you want to store the uploaded CSV. For example, `"data/uploaded_file.csv"`.

## Usage

1.  Ensure that the variables `service_account`, `file_path`, `bucket_name`, and `bucket_file_path` are set correctly.
2.  Run the script:

    ```bash
    python your_script_name.py
    ```

    The script will read the CSV file using pandas, upload it to the specified GCS bucket path, and print a confirmation message.

## Example

```python
import os.path
import pandas as pd
from google.cloud import storage

service_account = "my-service-account.json" # file with credentials

file_path = 'my_data.csv' # file name you want to upload
file_name = os.path.basename(file_path)
file = pd.read_csv(file_path)

bucket_name = "my-bucket" # bucket name you want to upload to
bucket_file_path = f"data/uploaded_data.csv" # bucket filepath and file name

storage_client = storage.Client.from_service_account_json(service_account)
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(bucket_file_path)
blob.upload_from_string(file.to_csv(index=False), content_type='text/csv')

print(f"{file_name} uploaded to {bucket_name}/{bucket_file_path}")
