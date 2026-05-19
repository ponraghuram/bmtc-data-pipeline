from pyspark import pipelines as dp
from pyspark.sql.functions import col, count, sum as spark_sum, udf
from pyspark.sql.types import BooleanType
import re

# Define email validation UDF
def is_valid_email(email):
    if email is None:
        return False
    return bool(re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email))

is_valid_email_udf = udf(is_valid_email, BooleanType())


# Create a sample source table with user_id and email columns
@dp.materialized_view(
    name="sample_users",
    comment="Sample table with user_id and email for testing"
)
def sample_users():
    data = [
        (1, "user1@example.com"),
        (1, "user1.alt@test.org"),
        (2, "invalid-email"),
        (2, "user2@domain.co.uk"),
        (3, "user3@sample.com"),
        (3, "not_an_email"),
        (3, None),
        (4, "user4@website.net"),
        (5, "bad@email@domain.com"),
        (5, "user5@valid.io")
    ]
    return spark.createDataFrame(data, ["user_id", "email"])


# Validate emails, group by user_id, and aggregate counts
@dp.materialized_view(
    name="user_email_validation",
    comment="Email validation results aggregated by user_id"
)
def user_email_validation():
    df = spark.read.table("sample_users")
    
    # Add validation column
    df_with_validation = df.withColumn("is_valid", is_valid_email_udf(col("email")))
    
    # Group by user_id and aggregate
    result = df_with_validation.groupBy("user_id").agg(
        count("*").alias("total_count"),
        spark_sum(col("is_valid").cast("int")).alias("valid_email_count")
    )
    
    return result
