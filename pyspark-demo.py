from pyspark.sql import SparkSession 


spark = SparkSession.builder.appName('test').getOrCreate()

df_pyspark = spark.read.csv('anime_messy_data.csv', header=True ,inferSchema=True)

df_pyspark.printSchema()