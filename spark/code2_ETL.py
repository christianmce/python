print("Number of data rows:", df.count())

df.printSchema() # or data.dtypes or df.columns

df.describe("class", "cap-shape", "cap-surface", "cap-color").show()

df.first() # or df.head(1) or df.show(1)

# -----------------------------------------------------  EXTRACT  READ FROM DATASOURCES -----------------------------------

def extract(spark: SparkSession, type: str, source: str):
    # Read data from mysql database
    if type=="JDBC":
       output_df =     spark.read.format("JDBC").options(url='jdbc:mysql://localhost/world',dbtable=source,driver='com.mysql.cj.jdbc.Driver',user='root',password='root').load()
       return output_df
    if type=="CSV":
    # read data from filesystem
       output_df = spark.read.format("CSV").options(header=True,inferSchema=True).load(source)
       return output_df

# -----------------------------------------------------  SPARK SQL LOAD CSV AND OUTPUT JSON ------------------------------

data_file = '/unacH/ventas_sucursal.csv'
sdfData = scSpark.read.csv(data_file, header=True, sep=",").cache()
gender = sdfData.groupBy('Gender').count()
print(gender.show())

sdfData.registerTempTable("sales")
output =  scSpark.sql('SELECT * from sales')
output.show()

output = scSpark.sql('SELECT * from sales WHERE `Unit Price` < 15 AND Quantity < 10')
output.show()

output.write.format('json').save('filtered.json')

output.coalesce(1).write.format('json').save('filtered.json')


