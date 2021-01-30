import json
import csv
import boto3
import os
import sys
import datetime
import uuid
from csv import writer

s3_resource = boto3.resource('s3')
first_bucket = 'datacoachtest'

def update_file(myParams):
    file_name = 'datacoach.json' 
    s3_resource.Object(first_bucket, file_name).download_file('/tmp/datacoach.json')
    
    with open('/tmp/datacoach.json', 'r') as f:
        data = json.load(f)
        print(type(data['responses']))
        data['responses'].append(myParams)
        print(data['responses'])
        f.close()
    with open('/tmp/datacoach.json', 'w') as f: 
        json_object = json.dumps(data)
        f.write(json_object)
        f.close()
    first_object = s3_resource.Object(bucket_name='datacoachtest', key=file_name)
    first_object.upload_file('/tmp/'+file_name)
    return str(file_name) + ' was created'

def lambda_handler(event, context):
    # TODO implement
    new_response ={"company_id": event['company_id'],"person_id": event['person_id'], "rating": event['rating'] }
    update_file(new_response)
    
    mystring = "Your company_id is: "+ event['company_id'] + " and you person_id is "+ event['person_id'] + " and the rating is " + event['rating']
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(mystring)
    }

