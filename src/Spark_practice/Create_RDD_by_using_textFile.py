from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("Reading the csv file").getOrCreate()

# Replace 'your_file_path.csv' with the actual path to your CSV file
file_path = 'E:/Spark_Assignment-1/Resource/user.csv'

# Read the CSV file into a DataFrame
df = spark.read.csv(file_path, header=False, inferSchema=False)

#Here i use header=False,inferSchema=False then it will Generate the Default Colimn name  for each column
#+-------+--------------------+--------------+---------+
# |    _c0|                 _c1|           _c2|      _c3|
# +-------+--------------------+--------------+---------+
# |user_id|             emailid|nativelanguage|location |
# |    101|   abc.123@gmail.com|         hindi|   mumbai|
# |    102|      jhon@gmail.com|       english|      usa|
# |    103|  madan.44@gmail.com|       marathi|   nagpur|
# |    104|local.88@outlook.com|         tamil|  chennai|
# |    105|  sahil.55@gmail.com|       english|      usa|
# |    106|       adi@gmail.com|         hindi|   nagpur|
# |    107|     jason@gmail.com|       marathi|   mumbai|
# |    108|     sohan@gmail.com|        kannad|      usa|
# |    109|    case@outlook.com|         tamil|   mumbai|
# |    110|      fury@gmail.com|         hindi|   nagpur|
# +-------+--------------------+--------------+---------+

df2 = spark.read.csv(file_path, header=True, inferSchema=True)
#Now we are taking header=true,and inferSchema=true then its takes our actuals data/column if we will mension true then it will not generate any defualt Column.

# +-------+--------------------+--------------+---------+
# |user_id|             emailid|nativelanguage|location |
# +-------+--------------------+--------------+---------+
# |    101|   abc.123@gmail.com|         hindi|   mumbai|
# |    102|      jhon@gmail.com|       english|      usa|
# |    103|  madan.44@gmail.com|       marathi|   nagpur|
# |    104|local.88@outlook.com|         tamil|  chennai|
# |    105|  sahil.55@gmail.com|       english|      usa|
# |    106|       adi@gmail.com|         hindi|   nagpur|
# |    107|     jason@gmail.com|       marathi|   mumbai|
# |    108|     sohan@gmail.com|        kannad|      usa|
# |    109|    case@outlook.com|         tamil|   mumbai|
# |    110|      fury@gmail.com|         hindi|   nagpur|
# +-------+--------------------+--------------+---------+

# heare i am using show method to show the Data frame(df) and data frame(df2)
df.show()
df2.show()

#To check the data type,constrants tye and column name  of each column or  read or print the schema we are using printSchema()
df.printSchema()
df2.printSchema()

# Stop the Spark session
spark.stop()
