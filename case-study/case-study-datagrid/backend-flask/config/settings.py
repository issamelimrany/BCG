import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATA_PATH = os.getenv("DATA_PATH")
