import os, subprocess, sys
import logging as lgm
from config import LOCAL
import datetime

FORMAT = "%(asctime)s | %(message)s"
lgm.basicConfig(level=lgm.INFO, format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

logging = lgm.getLogger()

tee = subprocess.Popen(
    ["tee", os.path.join(LOCAL.logs, f"TEST_{datetime.datetime.now()}.log")],
    stdin=subprocess.PIPE,
)
os.dup2(tee.stdin.fileno(), sys.stdout.fileno())
os.dup2(tee.stdin.fileno(), sys.stderr.fileno())
# file_handler = lgm.FileHandler(
#     os.path.join(LOCAL.logs, f"TEST_{datetime.datetime.now()}.log")
# )
# file_handler.setLevel(level=lgm.INFO)
# logging.addHandler(file_handler)
