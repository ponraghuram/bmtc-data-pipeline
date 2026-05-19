from pyspark import pipelines as dp
from pyspark.sql.functions import *

#creating empty streaming table
dp.create_streaming_table("total_sales")


#appending  North sales to total sales
@dp.append_flow(target='total_sales')
def north_sales():
    df = spark.readStream.table(" workspace.source.sales_north")
    return df

    #appending  south sales to total sales
@dp.append_flow(target='total_sales')
def sourth_sales():
    df = spark.readStream.table(" workspace.source.sales_sourth")
    return df