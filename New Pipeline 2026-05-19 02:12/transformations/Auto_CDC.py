from pyspark import pipelines as dp
from pyspark.sql.functions import *

#creating empty streaming table
dp.create_streaming_table("products_scd2")

#creating empty streaming table
dp.create_streaming_table("products_scd1")


#streaming view source
@dp.temporary_view
def products_source():
    df = spark.read.table('workspace.source.products')
    return df

#scd type 2
dp.create_auto_cdc_flow(
    target = "products_scd2",
    source = "workspace.source.products",
    keys=["product_id"],
    sequence_by = col("updated_at"),
    # apply_as_deletes =
    except_column_list =["updated_at"] ,
    stored_as_scd_type = "2"
)

#scd type 1
dp.create_auto_cdc_flow(
    target = "products_scd1",
    source = "workspace.source.products",
    keys=["product_id"],
    sequence_by = col("updated_at"),
    # apply_as_deletes =
    except_column_list =["updated_at"] ,
    stored_as_scd_type = "1"
)