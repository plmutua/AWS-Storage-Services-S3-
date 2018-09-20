import boto3

# To create an s3 client
s3 = boto3.client('s3')

# creates buckets in three regions
s3.create_bucket(Bucket='plmbucket1', CreateBucketConfiguration={
    'LocationConstraint': 'ap-south-1'})
s3.create_bucket(Bucket='plmbucket2', CreateBucketConfiguration={
    'LocationConstraint': 'eu-central-1'})
s3.create_bucket(Bucket='plmbucket3', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})

# Print command to verify successful execution 
print("Buckets created")