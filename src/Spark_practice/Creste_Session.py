from pyspark.sql import SparkSession

# first of all I Create SparkSession
spark = SparkSession.builder.getOrCreate()
# \
#.master("local[1]")
#\
#.appName("SparkByExamples.com") \
#.getOrCreate()

# Now I Create RDD from parallelize

dataList = [("kanhaiya Kumar", "Bihar",20), ("Satyam kumar", "Patna",24), ("gree","Andhra", 24)]
rdd=spark.sparkContext.parallelize(dataList)
dataColl=rdd.collect()
#Here i print all data

print(dataList)
