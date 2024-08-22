import boto3
import pandas as pd
import requests
from io import StringIO

def download_google_sheet(url):
    """Download the Google Sheet as CSV."""
    response = requests.get(url)
    response.raise_for_status()
    return StringIO(response.text)

def upload_to_s3(bucket_name, key, file_content):
    """Upload file content to S3 bucket."""
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=file_content)

def main():
    # Google Sheets URL (replace with the actual export URL)
    google_sheets_url = 'https://docs.google.com/spreadsheets/d/1zH0x0ZmBRIdJ0SrDcuWWma_82DfNy7qsyrWV4D_XVgc/export?format=csv'
    
    # S3 Bucket and Key
    bucket_name = 'rawfolder3327'
    s3_key = 'data.csv'
    
    # Download Google Sheet as CSV
    csv_file_content = download_google_sheet(google_sheets_url)
    
    # Upload CSV to S3
    upload_to_s3(bucket_name, s3_key, csv_file_content.getvalue())

if __name__ == "__main__":
    main()
