import boto3
import pandas as pd
import re
from io import StringIO

def read_from_s3(bucket_name, s3_key):
    """Read data from S3 bucket."""
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
    data = response['Body'].read().decode('utf-8')
    return StringIO(data)

def validate_headers(df, expected_headers):
    """Validate if the DataFrame headers match the expected headers."""
    if list(df.columns) != expected_headers:
        raise ValueError("Headers do not match the expected headers.")

def validate_data(df):
    """Perform data validation."""
    # Replace NaN values with empty strings
    df.fillna('', inplace=True)

    # Example: Regex validation for special characters in the 'location' column
    df['location'] = df['location'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

    return df

def write_to_s3(bucket_name, key, df):
    """Write DataFrame to S3 bucket as CSV."""
    s3_client = boto3.client('s3')
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=csv_buffer.getvalue())

def main():
    # S3 Bucket and Key
    input_bucket_name = 'rawfolder3327'
    input_s3_key = 'data.csv'
    output_bucket_name = 'updatedfolder3327'
    output_s3_key = 'updated_data.csv'
    
    # Read CSV data from S3
    csv_file_content = read_from_s3(input_bucket_name, input_s3_key)
    
    # Read CSV into DataFrame
    df = pd.read_csv(csv_file_content)
    
    # Expected headers
    expected_headers = ["location", "total_sqft", "bath", "price", "bhk"]
    
    # Validate headers
    validate_headers(df, expected_headers)
    
    # Validate data
    df = validate_data(df)
    
    # Write updated CSV to S3
    write_to_s3(output_bucket_name, output_s3_key, df)

if __name__ == "__main__":
    main()
