import os
from dotenv import load_dotenv

# __file__ is directory of this file
dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

IMAGE_METADATA_FILE = os.getenv(
    "IMAGE_METADATA_FILE") or "image_metadata.json"
IMAGE_METADATA_PATH = os.path.join(dirname, "data", IMAGE_METADATA_FILE)

IMAGE_FILES_PATH = os.path.join(dirname, "entities/image_files/")
SAMPLE_FILE_PATH = os.path.join(dirname, "entities/image_files/samples/")

DATABASE_FILE = os.getenv(
    "DATABASE_FILE") or "image_data.db"
DATABASE_FILE_PATH = os.path.join(dirname, "data", DATABASE_FILE)
