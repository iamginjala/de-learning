import boto3

client = boto3.client('s3')  # Uses your CLI-configured us-east-2 region
# response = client.create_bucket(
#     Bucket='demo-boto3-bucket-harsha-de',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'us-east-2'
#     }
# )

# print(response)

client.upload_file('aws_practice/hello.txt', 'demo-boto3-bucket-harsha-de', 'hello.txt')