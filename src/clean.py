import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src import db

file_path = 'data/raw/data.csv'  # Data must be in this location for the script to work

### Input received from data/raw
def input(file_path):
    # Read data from file
    data = pd.read_csv(file_path)
    return data

### If data == db, invoke db.py (PLACEHOLDERS)
def check(data):
    if data is sql:
        ### If data != db, continue
        db.receive(data)
    elif data is not sql:
        ### If data == db, FIX
        data = db.return_data()
    else:
        ### Edge case handling
        print("Error: Data format not recognized.")
    return data



### Clean data (PLACEHOLDERS)
def clean(data):
    # Remove duplicates
    data = data.drop_duplicates()
    # Handle missing values
    data = data.fillna(method='ffill')
    # Standardize formats
    # (Add specific formatting logic as needed)
    return data
### Return cleaned data to export.py

