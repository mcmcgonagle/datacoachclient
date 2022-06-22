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
    file_name = 'onefile.csv' 
    s3_resource.Object(first_bucket, file_name).download_file('/tmp/onefile.csv')
    
    with open('/tmp/onefile.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            print(row)
        f.close()

    with open('/tmp/onefile.csv', 'a') as f: 
        csv_writer = writer(f)
        csv_writer.writerow(myParams)
        f.close()
    first_object = s3_resource.Object(bucket_name='datacoachtest', key=file_name)
    first_object.upload_file('/tmp/'+file_name)
    return str(file_name) + ' was created'

def lambda_handler(event, context):
    new_response =[event['company_id'], event['person_id'], event['rating']]
    update_file(new_response)
    
    mystring = "Your company_id is: "+ event['company_id'] + " and you person_id is "+ event['person_id'] + " and the rating is " + event['rating']
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(mystring)
    }

