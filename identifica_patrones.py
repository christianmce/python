from puspark import SparkConf, SparkContext
conf = SparkConf.setMaster("local".setAppName("Miapp1")
sc = SparkContext(conf = conf)
lineas = sc.textFile("datosejemplo.txt")
py = sc.accumulator(0)
sp = sc.accumulator(0)
