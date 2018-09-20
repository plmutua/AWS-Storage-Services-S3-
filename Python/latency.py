import boto3
import botocore
import datetime

# Get the service client
s3 = boto3.resource('s3')
client = boto3.client('s3')

print "The bucket is in us-west-2 region"
bucket = ['plmbucket3']

# for loop to run the command 30 times
for i in range(1,31,1):
# Upload a file to the bucket and calculate the latency
	upload_starttime = datetime.datetime.now()
	with open("xerox.pdf", "rb") as f:
		client.upload_fileobj(f, 'plmbucket3', "xerox.pdf")
		upload_endtime = datetime.datetime.now()
		total_upload = upload_endtime-upload_starttime
		print i, "File upload is ", total_upload.total_seconds(), "seconds"


# Download a file from a bucket and calculate the latency speed
	download_starttime = datetime.datetime.now()
	with open("xerox.pdf", "wb") as f:
		client.download_fileobj('plmbucket3', "xerox.pdf", f)
		download_endtime = datetime.datetime.now()
		total_download = download_endtime-download_starttime
		print i, "File download is ", total_download.total_seconds(), "seconds\n"


 

