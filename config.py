import os
from dataclasses import dataclass

DEFAULT_SPARK_CONFIG = {"spark.app.name": "first Application", "spark.master": "local"}


@dataclass
class LOCAL:
    home = os.getcwd()

    files = os.path.join(home, "files/")

    logs = os.path.join(files, "logs/")
