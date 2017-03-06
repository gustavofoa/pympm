from boto.s3.connection import S3Connection

#Connect
conn = S3Connection('access key','secret')

#Get your bucket
b = conn.get_bucket('bucket')

#Iterate through bucket keys, set metadata and update your key
for key in b.list():
    key.metadata.update({'Cache-Control': 'max-age=3154000'})
    key.copy(
        key.bucket.name,
        key.name,
        key.metadata,
        preserve_acl=True)
    print('Cached -> ', key.name)
