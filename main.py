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

        # check existence of 'city' and 'price' columns
        required_cols = ['city', 'price']
        for col in required_cols:
            if col not in data.columns:
                raise ValueError(f"Missing required column: {col} in the CSV file.")
        return data

    except Exception as e:
        print(f"Error: {e}")
    
    return None

def create_report(data):
    # create report file with the following fields: city, avg price per city and total price per city 
    try:
        report = data.groupby('city').agg(
            avg_price_per_city = ("price", "mean"),
            total_price_per_city = ("price", "sum")
        ).reset_index()

        # save the report file
        report_file_name = "report.csv"
        report.to_csv(report_file_name, index = False)
        print(f"{report_file_name} file has been successfully created.")
    except Exception as e:
        print(f"Error while creating the report file: {e}")

def main():
    file_name = "Sacramentorealestatetransactions (1).csv"

    data = load_csv_file(file_name)

    if data is not None:
        create_report(data)

if __name__ == "__main__":
    main()