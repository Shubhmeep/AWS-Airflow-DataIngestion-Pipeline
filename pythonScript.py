import requests
import io
from datetime import date, timedelta
import os
import pandas as pd
import boto3
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
AWS_KEY=os.getenv("AWS_KEY")
AWS_SECRET_KEY=os.getenv("AWS_SECRET_KEY")
S3_BUCKET_NAME=os.getenv("S3_BUCKET_NAME")
CSV_FILE_NAME=os.getenv("CSV_FILE_NAME")
AWS_REGION=os.getenv("AWS_REGION")
CLEANED_CSV_FILE_NAME = os.getenv("CLEANED_CSV_FILE_NAME")
CLEANED_S3_BUCKET_NAME = os.getenv("CLEANED_S3_BUCKET_NAME")

def get_earthquakes(date=date.today()):
    params = {
        'format': 'csv',
        'starttime': date - timedelta(days=1),
        'endtime': date
    }

    r = requests.get(API_KEY, params=params)
    earthquakes_df = pd.read_csv(io.StringIO(r.text))
    return earthquakes_df


def filter_earthquakes(df):
    df = df[['id', 'time', 'latitude', 'longitude', 'depth', 'depthError', 'rms', 'status', 'type', 'mag']]
    df = df[df.type == 'earthquake']
    df['reviewed'] = (df['status'] == 'reviewed').astype(float)
    df.drop(columns=['type', 'status'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def extractData():
    earthquakes_df = pd.concat([filter_earthquakes(get_earthquakes(date(2022, 1, 1) - timedelta(i))) for i in range(50)])
    earthquakes_df.to_csv(CSV_FILE_NAME, index=False)

    return 'FILE EXECUTION DONE'


def pushToS3(AWS_REGION,AWS_KEY,AWS_SECRET_KEY,S3_BUCKET_NAME,CSV_FILE_NAME):

    s3 = boto3.resource(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    s3.Bucket(S3_BUCKET_NAME).upload_file(Filename=CSV_FILE_NAME, Key=CSV_FILE_NAME)

    return 'CSV FILE PUSHED TO S3'


def getCleanedDataFromS3(AWS_REGION,AWS_KEY,AWS_SECRET_KEY,CLEANED_S3_BUCKET_NAME,CLEANED_CSV_FILE_NAME):

    s3 = boto3.resource(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    
    s3.Bucket(CLEANED_S3_BUCKET_NAME).download_file(Key=CLEANED_CSV_FILE_NAME, Filename=CLEANED_CSV_FILE_NAME)

    return 'CLEAN DATA DOWNLOADED FROM S3'


def removeTestDataFromDirectory(CSV_FILE_NAME):
    if os.path.exists(CSV_FILE_NAME):
        os.remove(CSV_FILE_NAME)
        return f"{CSV_FILE_NAME} has been successfully deleted."
    else:
        return f"{CSV_FILE_NAME} does not exist in the directory."







