import os
import pandas as pd


def load_csv_file(file_name: str):
    try:
        # get the file path dynamically
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, file_name)

        # check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_name} was not found.")
        
        # load the csv file
        data = pd.read_csv(file_path)

    except Exception as e:
        print(f"Error: {e}")
    
    return None

def main():
    file_name = "Sacramentorealestatetransactions (1).csv"

    data = load_csv_file(file_name)