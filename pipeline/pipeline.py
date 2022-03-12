from utils.logging import logging
from utils.spark import getOrCreateSparkSession
from config import LOCAL
from utils.python import clean


class Pipeline:
    """

    Pipeline class

    """

    def __init__(self, spark=None):
        # Create spark session in case it was not created before
        if spark is None:
            spark = getOrCreateSparkSession()
        self.spark = spark
        logging.info(f"Test spark {self.spark.sparkContext.getConf().getAll()}")

    def first_pipeline(self):
        """
        Run first pipeline

            Parameters:
                    self

            Returns:
                    None
        """
        logging.info("Start first pipeline")
        logging.info(f"{LOCAL.logs}")

        # Clean up log files
        clean(LOCAL.logs)
