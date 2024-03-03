# Seismic Magnitude Prediction: An Automated ML Pipeline for Earthquake Analysis using ANSS Data API

## Introduction - Data Ingestion Pipeline Description
Herein lies the detailed breakdown of the meticulously crafted data ingestion pipeline microservice, engineered to seamlessly handle the flow of data from its raw form to a state primed for machine learning model training. This pipeline has been deployed and operationalized on an EC2 instance, leveraging the robust capabilities of Apache Airflow for orchestrating each stage of the process.

<p align="center">
  <img src="https://github.com/Shubhmeep/AWS-Airflow-DataIngestion-Pipeline/assets/97219802/9a4db5a1-4d35-4e65-bfce-0cdd5d62b9ee" width="800" alt="Data Ingestion Pipeline Image">
</p>

In the Above architecture that i've created using [Lucidcharts](https://lucid.app/lucidchart/57b8e7c4-3203-46e1-b205-e510b7ca170e/edit?viewport_loc=728%2C877%2C2853%2C1259%2C.Q4MUjXso07N&invitationId=inv_279445a0-7953-4521-bf35-7309b1fbc793) This rope consists of the data-ingestion pipeline (a seperate microservice). explanation for how the pipeline is working is as follows:

### Airflow Deployment on EC2:
The foundational infrastructure for our data ingestion pipeline is hosted on an EC2 instance, where the Airflow web server is deployed. Airflow provides an intuitive interface to define, schedule, and monitor workflows, ensuring the smooth execution of each task within the pipeline.

### Data Retrieval from API:
The journey commences with the extraction of raw data from a designated API source. Leveraging Airflow's extensible architecture, this task is orchestrated to execute at predetermined intervals, ensuring the continuous ingestion of fresh data into the pipeline.

### Data Formatting and Transformation:
With raw data in hand, the pipeline applies necessary formatting adjustments and transformations to align the data with the desired schema. This crucial step ensures consistency and compatibility across the dataset, laying the groundwork for downstream processing.

### Raw Data Archival to S3:
Processed raw data is seamlessly archived onto Amazon S3, a highly scalable and durable cloud storage solution. This task ensures the reliable storage of raw data, paving the way for subsequent processing stages.

### Triggering Lambda Function for Pre-Processing:
Upon archival of raw data, a Lambda function is dynamically triggered, initiating pre-processing operations. This event-driven architecture ensures prompt action upon data arrival, facilitating timely data preparation for downstream analysis.

### Post-Processing and Storage in Final S3 Bucket:
Upon completion of pre-processing operations, the refined data is stored in the final S3 bucket. Through the invocation of another Lambda function, this task ensures that the processed data is readily accessible for training machine learning models, culminating in actionable insights and informed decision-making.

## Conclusion:
In essence, this meticulously crafted data ingestion pipeline embodies the convergence of robust infrastructure, efficient orchestration, and scalable processing capabilities. By adhering to best practices in data engineering and leveraging automation and cloud technologies, this pipeline streamlines the data lifecycle, from ingestion to insight, driving transformative outcomes for data-driven decision-making.

To know about the next feature pipeline and training pipeline visit the repository - https://github.com/Shubhmeep/Earthquake-prediction-ML-pipeline.git

## Disclaimer:

Please note that this Airflow project is configured entirely on an EC2 instance. Therefore, individuals interested in utilizing this project must set up their own EC2 instance and establish Secure Socket Layer (SSL) access to it. Additionally, appropriate AWS access permissions must be configured for the root user to interact with AWS services.

It's important to highlight that the instance access keys used for this project cannot be shared. The current deployment utilizes a t2.medium instance type, and the owner is responsible for the associated costs incurred from AWS.

We advise users to follow AWS best practices and guidelines when setting up their EC2 instance and configuring access permissions. Any misuse or unauthorized access to AWS resources is the sole responsibility of the user.

Thank you for your understanding and cooperation.
