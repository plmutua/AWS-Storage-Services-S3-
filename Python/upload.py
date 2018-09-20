import boto3

# Create an S3 client
s3 = boto3.client('s3')

filename = 'bird.jpg'
bucket_name = 'plmbucket1'

# Uploads file 
s3.upload_file(filename, bucket_name, filename)
print("File uploaded")