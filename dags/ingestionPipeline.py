from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
import requests
import io,os 
import boto3
from datetime import date, timedelta, datetime

import sys
sys.path.append('/home/ubuntu/airflow')
from pythonScript import extractData, pushToS3, getCleanedDataFromS3, removeTestDataFromDirectory

import pandas as pd 

from dotenv import load_dotenv
load_dotenv()


default_args = {
    'owner': 'shubh-airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 28),
    'email': ['shubh.sehgal2506@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=15)
}

with DAG('dataIngestionDag',
        default_args=default_args,
        schedule_interval = '@daily',
        catchup=False) as dag:


        extract_data_var = PythonOperator(
        task_id= 'task_extract_earthquake_data',
        python_callable=extractData
        )

        push_to_s3 = PythonOperator(
            task_id = 'push_csv_to_s3',
            python_callable=pushToS3,

            op_kwargs={
            'AWS_REGION': os.getenv("AWS_REGION"),
            'AWS_KEY': os.getenv("AWS_KEY"),
            'AWS_SECRET_KEY': os.getenv("AWS_SECRET_KEY"),
            'S3_BUCKET_NAME': os.getenv("S3_BUCKET_NAME"),
            'CSV_FILE_NAME': os.getenv("CSV_FILE_NAME")
        }
        )

        remove_test_data_from_directory = PythonOperator(
            task_id = 'remove_test_data_from_directory',
            python_callable = removeTestDataFromDirectory,

            op_kwargs = {
                 'CSV_FILE_NAME': os.getenv("CSV_FILE_NAME")
            }
            
        )

        get_cleaned_data_from_s3 = PythonOperator(

            task_id = 'get_clean_csv_from_s3',
            python_callable=getCleanedDataFromS3,

            op_kwargs={
            'AWS_REGION': os.getenv("AWS_REGION"),
            'AWS_KEY': os.getenv("AWS_KEY"),
            'AWS_SECRET_KEY': os.getenv("AWS_SECRET_KEY"),
            'CLEANED_S3_BUCKET_NAME': os.getenv("CLEANED_S3_BUCKET_NAME"),
            'CLEANED_CSV_FILE_NAME': os.getenv("CLEANED_CSV_FILE_NAME")
        }

        )

        extract_data_var >> push_to_s3 >> remove_test_data_from_directory >> get_cleaned_data_from_s3


