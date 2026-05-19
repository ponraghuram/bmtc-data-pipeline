from pyspark.sql.functions import udf
import re
from pyspark.sql.types import BooleanType

def is_valid_email(email):
    if email is None:
        return False
    return bool(re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email))

is_valid_email_udf = udf(is_valid_email, BooleanType())