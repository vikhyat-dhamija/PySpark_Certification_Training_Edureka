import sys
import os
import random
from operator import add, mul
from pyspark import SparkContext, SparkConf
from pyspark import SparkFiles
import time

def main(arg):
    file = arg
    conf = SparkConf().setAppName("HdfsTest")
    sc = SparkContext(conf=conf)
    rdd = sc.textFile(file).map(lambda line: len(line))

    for iter in range(10):
        start=time.time()
        rdd.map(lambda x : x+2) 
        duration=time.time()-start
        print("Iteration took this much time : ", duration)
        print("Returned length(s) of: " , rdd.sum())
        

if __name__=="__main__":
    main(sys.argv[1])