import boto3

s3 = boto3.resource('s3')

def s3_list():
    bucket_list = []
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucket_list.append(bucket.name)
    return(bucket_list)

def s3_bucket_size(bucket):
    sizeB=0
    my_bucket=s3.Bucket(bucket)
    for object in my_bucket.objects.all():
        print(object.key)
        sizeB = sizeB + object.size
        TotalGB = sizeB / 1000 / 1024 / 1024
    print(sizeB, "Bytes")
    print("Total Size: ", TotalGB)

if __name__ == '__main__':
    #List Buckets
    print("\nBucket List")
    print(s3_list())
    #List Size of objects in a bucket and it's total size
    print("\nObjects/Sizes and Total Bucket Size")
    s3_bucket_size('elasticbeanstalk-ap-southeast-2-539615378239')
