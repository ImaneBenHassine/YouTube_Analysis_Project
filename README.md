# YouTube AnalysisProject

## Introduction
In this project, we will execute an end-to-end data engineering project from getting data to building final dashboard by managing, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.

so consider we have a Client or company who wants to run some ad campaign online and they selected their main advertising channel 
as youtube they want to understand some of the initial question they have such as how to categorize videos based on their comments and
statistics what are the factors affect how popular a youtube video will be these are the things they want to
understand before actually investing money in the youtube campaign.


## Technologies 

- **Amazon S3**: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
- **AWS Glue**: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
- **AWS IAM**: This is nothing but identity and access management which enables us to manage access to AWS services and resources securely.
- **AWS Lambda**: Lambda is a computing service that allows programmers to run code without creating or managing servers.
- **AWS Athena**: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.
- **QuickSight**: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.

## Steps

- build a data lake from scratch using Amazon S3 : joining semi-structured and structured 
- build AWS Catalog we will use Glue for Cataloging 
- write ETL JOB in AWS Glue Spark job In Lambda and Cleaning Data
- write SQL queries using Amazon Athena & Spark SQL
- write script to ingest data incrementally and understand how to build a proper schema 
- build a BI dashboard in Amazon QuickSight
