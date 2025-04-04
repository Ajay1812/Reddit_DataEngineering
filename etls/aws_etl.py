import boto3
from utils.constants import AWS_ACCESS_KEY, AWS_ACCESS_KEY_ID, AWS_REGION

def connect_to_s3():
    try:
       s3 = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_ACCESS_KEY,
                region_name=AWS_REGION
            )
       print('connected to s3')
       return s3
    except Exception as e:
        print("ERROR: ", e)


def create_bucket_if_not_exist(s3,bucket):
    try:
        if not boto3.resource('s3'):
            s3.create_bucket(Bucket=bucket, createBucketConfiguration={'LocationConstraint': AWS_REGION})
            print("Bucket is created")
        else:   
            print("Bucket already exists")
    except Exception as e:
        print(e)        

def upload_to_s3(s3 : boto3.client, file_path: str, bucket: str, s3_fle_name:str):
    try:
        s3.upload_file(file_path, bucket+'/raw/' , s3_fle_name)
        print(f"✅ Uploaded '{file_path}' to bucket '{bucket}' as '{s3_fle_name}'")
    except Exception as e:
        print(f"❌ Upload failed: {e}")
