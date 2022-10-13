#Autor: Dr. Christian Mauricio Castillo Estrada <cmce@unach.mx>
#Facultad de Negocios CIV UNACH - LIDTS

import findspark
import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

findspark.init()

sparkConf = SparkConf().setAppName("SparkQL App Ventas")
sc = SparkContext(conf=sparkConf)
spark = SparkSession(sc)

dataset1 = spark.read.load("prueba1.csv",
                          format="csv",
                          sep=",",
                          inferSchema="true",
                          header="true")


dataset1.printSchema()
dataset1.show(7)

spark.stop()
