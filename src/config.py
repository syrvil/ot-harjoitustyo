import os
from dotenv import load_dotenv

# __file__ is directory of this file
dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

IMAGE_FILENAME = os.getenv("IMAGE_FILENAME") or "images.json"
IMAGE_FILE_PATH = os.path.join(dirname, IMAGE_FILENAME)