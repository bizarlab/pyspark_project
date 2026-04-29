from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

df = spark.read.csv('/home/iosu/github-repos/pyspark_project/data/ventas.csv',
                    header=True,
                    inferSchema=True,
                    sep=",")

df.show()
df.printSchema()

