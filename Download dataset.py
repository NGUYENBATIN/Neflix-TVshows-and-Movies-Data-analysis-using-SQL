import kagglehub
import os
import shutil


# 1. Download the Netflix dataset to the system's default cache directory
cache_path = kagglehub.dataset_download("shivamb/netflix-shows")

# 2. Define the destination directory (Your current working directory in VS Code)
current_dir = os.getcwd() 

# 3. Retrieve files from the cache directory and move them to the current directory
for file_name in os.listdir(cache_path):
    source_file = os.path.join(cache_path, file_name)
    destination_file = os.path.join(current_dir, file_name)
    
    # Move the file (Will overwrite if the file already exists)
    shutil.move(source_file, destination_file)
    print(f"File successfully saved to working directory: {destination_file}")
import pandas as pd

# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv')
df.info()

# LOAD DATA TO DATABASE
import pandas as pd
from sqlalchemy import create_engine

# 1. Read the CSV file directly from your current active workspace
df = pd.read_csv('netflix_titles.csv')

