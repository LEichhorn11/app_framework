import os
from utils.logging import logging


def clean(path):
    """
        Drop all files located in the path.

                Parameters:
                        path (str): A string with the location of the files to drop

    """
    try:
        files = f"{path}*"

        os.system(f"rm -rf {files}")
        logging.info(f"Remove all files in {files}")
    except:
        logging.warn(f"Path {files} does not exist")
