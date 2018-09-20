import boto3
import botocore
import datetime

# Allows to use Amazon s3 and create a client
s3 = boto3.resource('s3')
client = boto3.client('s3')

regions=['eu-central-1', 'ap-south-1']

# List all buckets in ap-south-1 region
for bucket in s3.buckets.all():
	bucket_name = bucket.name
	location = dict()
	location = client.get_bucket_location(Bucket=bucket_name)
	if location['LocationConstraint'] == 'ap-south-1':
		print "Bucket {} is from ap-south-1".format(bucket_name)




