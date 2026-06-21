
from pyspark.sql import Row
apps=["Payment Platform","Customer Portal","Fraud Engine"]
df=spark.createDataFrame([Row(application=a) for a in apps])
df.write.mode("overwrite").saveAsTable("bronze_applications")
print("Sample data generated")
