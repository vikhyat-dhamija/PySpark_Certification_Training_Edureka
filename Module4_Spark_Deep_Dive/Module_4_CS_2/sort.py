from __future__ import print_function
import sys,time
from pyspark.sql import SparkSession
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: hdfstest.py <file>", file=sys.stderr)
        exit(-1)
    spark = SparkSession\
        .builder\
        .appName("HdfsTest_py")\
        .getOrCreate()
    file_ = spark.read.text(sys.argv[1]).rdd
    mapped = file_.map(lambda s:len(s)).cache()
    for i in range(10):
        start_time = time.time()
        mapped.map(lambda x: x+2)
        end_time = time.time()
        print('----> Iteration took:', end_time - start_time,'ms')
    spark.stop()
