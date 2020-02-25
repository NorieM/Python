import boto3

s3 = boto3.client('s3', aws_access_key_id='AKIAUTOI6SQWBMXB7TUJ',aws_secret_access_key='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')

rs = s3.list_buckets()

for bckt in rs['Buckets']:
    print(bckt['Name'])

with open('testfile.txt', 'rb') as f:
    s3.upload_fileobj(f, 'testbucket-norie', f.name)