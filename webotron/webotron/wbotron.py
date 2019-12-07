import boto3
import click
session = boto3.Session(profile_name='python-automation')
s3 = session.resource('s3')    

@click.group()
def cli():
    "Webotron deployes websites to aws"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all the s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
#@click.option('--bucketname', prompt='Bucket Name')
@click.argument('bucketname')
def list_bucket_objects(bucketname):
    "List objects in a s3 bucket"
    for obj in s3.Bucket(bucketname).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()
    
