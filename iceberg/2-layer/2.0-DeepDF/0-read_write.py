from pyspark.sql import SparkSession

# Build session

spark = SparkSession.builder\
        .appName("my-app")\
        .config("spark.some.config.option","some-value")\
        .getOrCreate()

# Read csv

# Write CSV