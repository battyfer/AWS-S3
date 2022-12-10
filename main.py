import boto3



## Create buckets
client = boto3.client('s3')
client.create_bucket(Bucket = "battyfer")




## Print the available buckets
response = client.list_buckets()
print(response['Buckets'])



## Uploading Files
def uploading(file_name, bucket, object_name = None, args = None):
    """
        file_name = local file name 
        bucket = name of bucket
        object_name = name of the file to shown on aws
        args = extra args
    """

    if object_name == None:
        object_name = file_name
        
    response = client.upload_file(file_name, bucket, object_name, ExtraArgs = args)

    print(response)

uploading('testData/images.jpg', 'battyfer')



## Uploading multiple files in a folder

import glob

files = glob.glob('testData/*')
print(files)
for file in files:
    uploading(file, 'battyfer')
    print('uploaded - ', file)


## to give public access
args = {'ACL' : 'public-read'}



## Download files from S3

s3 = boto3.resource('s3')
print(list(s3.buckets.all()))

print(client.list_buckets())

bucket = s3.Bucket('battyfer')

files = list(bucket.list.object.all())

for file in files:






# hash - string 
# bytes - bytes 
# hash_list - list of string 
# byte_list - list of bytes 

