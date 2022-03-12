import findspark

findspark.init("/opt/homebrew/lib/python3.8/site-packages/pyspark")

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from config import DEFAULT_SPARK_CONFIG


def getOrCreateSparkSession(SPARK_CONFIG=DEFAULT_SPARK_CONFIG):
    """
    Creates a new spark session.

            Parameters:
                    SPARK_CONFIG (dict): A dictionary including spark configs

            Returns:
                    spark session
    """
    conf = SparkConf(SPARK_CONFIG)
    return SparkSession.builder.config(conf=conf).getOrCreate()
