import boto3
from botocore.exceptions import ClientError

# Create an S3 client
s3 = boto3.client('s3')

bucketName = 'battyfer'

# Create the bucket
response = s3.create_bucket(Bucket = bucketName)
## print(response)

# Set the name of the file you want to upload
# file = 'data.txt'


def put_chunk(hash, bytes):
    
    try:
        # Create the object metadata
        metadata = {
            'hash': hash
        }

        # to give public access
        # args = {'ACL' : 'public-read'}

        # Upload the file to the bucket
        response = s3.put_object(Bucket = bucketName, Key = hash, Body = bytes, Metadata = metadata)
        # print(response)
        return True
    except Exception as e:
        print(e)



def get_chunk(hash):

    try:
        # Retrieve the object from the bucket
        response = s3.get_object(Bucket = bucketName, Key = hash)

        # Get the object's metadata
        metadata = response['Metadata']

        # Get the object's hash value
        hash_obj = metadata['hash']

        # Check if the hash matches the expected value
        if hash_obj == hash:
            # Get the object's data
            value = response['Body'].read()
            print('Hash found')
            print('data - ', value)
            return True
        else:
            print('Error: Hash not found')
            return False
        
    except Exception as e:
        print(e)


def chunk_exists(hash):

    try:
        response = s3.head_object(Bucket = bucketName, Key = hash)
        return True

    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            return False
        else:
            raise



put_chunk('1234567890abcdef', b'Hello, world!')
put_chunk('secondchunkkkk', b'randon dataa hereee')
get_chunk('1234567890abcdef')
get_chunk('1234567890')
print(chunk_exists('1234567890abcdef'))
print(chunk_exists('1234567890abcdef324'))














