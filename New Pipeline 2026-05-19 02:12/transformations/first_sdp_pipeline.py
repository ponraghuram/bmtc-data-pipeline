from pyspark import pipelines as dp
from pyspark.sql.functions import *

#Materialized view

@dp.materialized_view(name = "src")
def src_sales():
    df = spark.read.table("workspace.default.sample_users")
    return df

#materizalid view (referrring to another MV)

@dp.materialized_view(name = "enr_sales")
def online_sales():
    df = spark.read.table("workspace.default.src")
    df = df.withColumn("phone_number",lit(''))
    return df