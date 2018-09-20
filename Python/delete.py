import boto3

# Create an S3 client
client = boto3.client('s3')

# Deletes file 
client.delete_object(Bucket='plmbucket1', Key='bird.jpg')
print("File deleted")