import pandas as pd
from pymongo import MongoClient
import json

# Load the data
file_path = "src/data/Updated_sales.csv"
data = pd.read_csv(file_path)

# Convert 'Period' column to datetime
data["Period"] = pd.to_datetime(data["Period"]).dt.strftime("%Y-%m-%d %H:%M:%S")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sales"]  # Create or connect to a database
collection = db["retail_data"]  # Create or connect to a collection

# Convert DataFrame to JSON
data_json = json.loads(data.to_json(orient="records"))

# Insert data into MongoDB
collection.insert_many(data_json)


# 2024-03-04T12:13:34.401+00:00
# yyy%mm%
