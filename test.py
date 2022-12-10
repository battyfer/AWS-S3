import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create the bucket
response = s3.create_bucket(Bucket = 'battyfer-2')

print(response)

# Set the name of the bucket you want to upload to
bucketName = 'battyfer-2'

# Set the name of the file you want to upload
file = 'text_file_to_add_data.txt'

# Set the contents of the file
body = b'Hello, world!'

# Set the hash value for the file
hash = '1234567890abcdef'

# Create the object metadata
metadata = {
  'hash': hash
}

## to give public access
args = {'ACL' : 'public-read'}

# Upload the file to the bucket
response = s3.put_object(
  Bucket=bucketName,
  Key = file,
  Body=body,
  Metadata=metadata
)

print(response)