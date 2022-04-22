from pyspark import SparkConf, SparkContext
conf = SparkConf.setMaster("local".setAppName("Miapp1")
sc = SparkContext(conf = conf)
lineastxt = sc.textFile("datosejemplo.txt")
py = sc.accumulator(0)
sp = sc.accumulator(0)

def idenpatrones(linea):
	global py,sp
	if "Python" in linea:
		py+=1
		if "Spark" in linea:
			sp+=1
		return True
	if "Spark" in linea:
		sp+=1
		return True
	else:
		return False

valores = lineastxt.filter(idenpatrones)

valores.collect()
print(py)
print(sp)
