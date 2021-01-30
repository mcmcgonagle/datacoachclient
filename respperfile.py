import json
import csv
import boto3
import os
import sys
import datetime
import uuid

s3_resource = boto3.resource('s3')
first_bucket = s3_resource.Bucket(name='datacoachtest')

    
def create_file(params):
    id = uuid.uuid4().hex[:6]
    my_time=datetime.datetime.now()
    fmt="%Y_%m_%d_%H_%M_%S"
    file_name = str(id+'_feedback_'+my_time.strftime(fmt)+'.csv') 
    with open('/tmp/'+file_name, 'w') as f:
        f.write('compamy_id,person_id,rating,\n')
        f.write(params)
        f.close()
    first_object = s3_resource.Object(bucket_name='datacoachtest', key=file_name)
    first_object.upload_file('/tmp/'+file_name)
    return str(file_name) + ' was created'

def lambda_handler(event, context):
    # TODO implement
    company_id = event['company_id']
    person_id = event['person_id']
    rating = event['rating']
    s=','
    sequence=company_id,person_id,rating
    myParams= s.join(sequence)
    create_file(myParams)
    
    mystring = "Your company_id is: "+ company_id + " and you person_id is "+ person_id + " and the rating is " + rating
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(mystring)
    }
