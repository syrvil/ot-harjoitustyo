import os
from dotenv import load_dotenv

# __file__ is directory of this file
dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

IMAGE_METADATA_FILE = os.getenv("IMAGE_METADATA_FILE") or "images_metadata.json"
IMAGE_MEDATA_PATH = os.path.join(dirname, "entities", IMAGE_METADATA_FILE)
IMAGE_FILES_PATH = os.path.join(dirname, "entities", "images/")