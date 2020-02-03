from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My APP")
sc = SparkContext(conf = conf)