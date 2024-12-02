from dotenv import load_dotenv
import os
from pymongo import MongoClient

try:
    db_client = MongoClient(os.getenv("DATABASE_URL"))
    print("***************coneccion realizada**********")
except Exception as e:
    print(f"error al conectarse{e}")