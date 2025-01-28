import os
import pandas as pd

# get the file path dynamically
file_name = "Sacramentorealestatetransactions (1).csv"
current_directory = os.getcwd()
file_path = os.path.join(current_directory, file_name)
# load the csv file
data = pd.read_csv(file_path)