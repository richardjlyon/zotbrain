import time
from rich.progress import track
from rich import print
from rich.logging import RichHandler
import logging

FORMAT = "%(message)s"
logging.basicConfig(level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

for i in track(range(20), description="For example:"):
    time.sleep(0.05)