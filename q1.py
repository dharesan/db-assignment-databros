import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import FloatType


# you may add more import if you need to


# don't change this line
hdfs_nn = sys.argv[1] 

spark = SparkSession.builder.appName("Assigment 2 Question 1").getOrCreate()
# YOUR CODE GOES BELOW

# Read from HDFS
input_path = f"hdfs://{hdfs_nn}:9000/assignment2/part1/input/TA_restaurants_curated_cleaned.csv"

df = spark.read.csv(input_path, header=True)

df = df.filter(col("Reviews").isNotNull() & (col("Reviews") != ""))
df = df.filter(col("Rating").cast(FloatType()) >= 1.0)

output_path = f"hdfs://{hdfs_nn}:9000/assignment2/output/question1/"
df.write.mode("overwrite").csv(output_path, header=True)

spark.stop()