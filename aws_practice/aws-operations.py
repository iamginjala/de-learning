import boto3
import os

folder = 'C:/Users/hr242/Desktop/de-learning/aws_practice'
filename = 'downloaded_s3_file.txt'

full_path = os.path.join(folder, filename)


client = boto3.client('s3')  # Uses your CLI-configured us-east-2 region
# response = client.create_bucket(
#     Bucket='demo-boto3-bucket-harsha-de',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'us-east-2'
#     }
# )

# print(response)

## uploading files to s3

# client.upload_file('aws_practice/hello.txt', 'demo-boto3-bucket-harsha-de', 'hello.txt')

## listing all s3 buckets

# response = client.list_buckets()

# if response['Buckets']:
#     print("Buckets found:")
#     for bucket in response['Buckets']:
#         print(bucket['Name'])
# else:
#     print("No buckets found.")

## list all objects from s3
response = client.list_objects(Bucket = 'demo-boto3-bucket-harsha-de')

if response['Contents']:
    for obj in response['Contents']:
        print(obj['Key'])

## download_file 
client.download_file('demo-boto3-bucket-harsha-de','hello.txt',full_path)