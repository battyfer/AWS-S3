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

def chunk_exists(hash):
    
    try:
        response = s3.head_object(Bucket = bucketName, Key = hash)
        return True

    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            return False
        else:
            raise



def put_multiple_chunks(hash_list, bytes_list):
        
    try:
        for i in range(len(bytes_list)):

            key = hash_list[i]

            value = bytes_list[i]

            # Set the metadata for the object
            metadata = {
                'hash': hash_list[i]
            }

            # Upload the object to S3
            s3.put_object(Bucket = bucketName, Key = key, Body = value, Metadata = metadata)
        print('Data uploaded')

    except Exception as e:
        print(e)



def get_multiple_chunks(hash_list):

    bytes_list = []

    try:
        for hash in hash_list:
            key = hash

            response = s3.get_object(Bucket = bucketName, Key = key)

            metadata = response['Metadata']

            hash_obj = metadata['hash']

            if hash_obj == key:
                value = response['Body'].read()
                bytes_list.append(value)
            else:
                print('Error: Hash not found')
        
        return bytes_list

    except Exception as e:
        print(e)





hashValues = ['abc123', 'def456', 'ghi789', 'asjdashb']
dataChunks = [b'chunk1', b'chunk2', b'chunk3', b'chunk4']
put_multiple_chunks(hashValues, dataChunks)

print(chunk_exists('abc123'))
print(chunk_exists('asjdashb'))
print(chunk_exists('asjddsfdsfsd'))
