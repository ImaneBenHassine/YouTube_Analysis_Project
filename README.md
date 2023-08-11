# YouTube Analysis Project

## Introduction
In this project, we will execute an end-to-end data engineering project from getting data to building final dashboard by managing, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.

## Project Goals
We have this Client who wants to run some ad campaign online and they selected their main advertising channel as **youtube**. They want to understand some of the initial question before actually investing money in the youtube campaign : *how to categorize videos based on their comments and statistics ? what are the factors affect how popular a youtube video will be?*

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

## Dataset

This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. 

The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.

https://www.kaggle.com/datasets/datasnaek/youtube-new
