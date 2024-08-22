import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1724337034985 = glueContext.create_dynamic_frame.from_catalog(database="demo", table_name="demoupdatedfolder3327", transformation_ctx="AmazonS3_node1724337034985")

# Script generated for node Amazon Redshift
AmazonRedshift_node1724337338731 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3_node1724337034985, connection_type="redshift", connection_options={"redshiftTmpDir": "s3://aws-glue-assets-506572490930-ap-south-1/temporary/", "useConnectionProperties": "true", "dbtable": "public.realestate", "connectionName": "Redshift connection", "preactions": "CREATE TABLE IF NOT EXISTS public.realestate (location VARCHAR, total_sqft DOUBLE PRECISION, bath BIGINT, price DOUBLE PRECISION, bhk BIGINT);"}, transformation_ctx="AmazonRedshift_node1724337338731")

job.commit()