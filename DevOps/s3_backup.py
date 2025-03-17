"""
this is a script to take a backup from local to AWS S3

boto3 -> used to do aws tasks using python
"""
import boto3



s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


def create_bucket(s3,bucket_name, region):
    s3.create_bucket(Bucket=bucket_name,
                      CreateBucketConfiguration={
                          'LocationConstraint': region,
                       })
    print("Bucket created successfully!")


def upload_backup(s3,file_name,bucket_name, key_name):


    """
    uploads a given backup file path to a given s3 bucket 
    with a new name(key)


    """

    data = open(file_name, 'rb')  #binary me read hoga
    s3.Bucket(bucket_name).put_object(key=key_name, Body=data) #key is the name of the file in the bucket
    print("File uploaded successfully!")
  

bucket_name = "python-for-devops-junoon"
region = "us-west-2"

#create_bucket(s3, bucket_name, region)
#show_buckets(s3)

filename = "C:\\Users\\himan\\OneDrive\\Desktop\\Python\\DevOps\\Backup\\backup_" \
"2021-09-28.tar.gz"
 
upload_backup(s3, filename, bucket_name, "backup_2021-09-28.tar.gz") #key is the name of the file in the bucket