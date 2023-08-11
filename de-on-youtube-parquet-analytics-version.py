import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1691744309909 = glueContext.create_dynamic_frame.from_catalog(
    database="de_youtube_cleaned",
    table_name="raw_statistcs",
    transformation_ctx="AWSGlueDataCatalog_node1691744309909",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1691744304869 = glueContext.create_dynamic_frame.from_catalog(
    database="de_youtube_cleaned",
    table_name="cleaned_statistics_reference_data",
    transformation_ctx="AWSGlueDataCatalog_node1691744304869",
)

# Script generated for node Join
Join_node1691744370841 = Join.apply(
    frame1=AWSGlueDataCatalog_node1691744309909,
    frame2=AWSGlueDataCatalog_node1691744304869,
    keys1=["category_id"],
    keys2=["id"],
    transformation_ctx="Join_node1691744370841",
)

# Script generated for node Amazon S3
AmazonS3_node1691744511598 = glueContext.getSink(
    path="s3://de-on-youtube-analytics-eu-west-3-dev/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "category_id"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1691744511598",
)
AmazonS3_node1691744511598.setCatalogInfo(
    catalogDatabase="db_youtube_analytics", catalogTableName="final_analytics"
)
AmazonS3_node1691744511598.setFormat("glueparquet")
AmazonS3_node1691744511598.writeFrame(Join_node1691744370841)
job.commit()
