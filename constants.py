import os
from os import path
from dotenv import load_dotenv
load_dotenv()

LOG_FILENAME = os.getenv("LOG_FILENAME")
LOG_FILEPATH = path.join(path.dirname(__file__), LOG_FILENAME)

filepath = os.getenv("LOG_FILEPATH")
if filepath:
    LOG_FILEPATH = path.join(filepath, LOG_FILENAME)