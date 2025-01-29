import os
import pandas as pd
import numpy as np


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

def clean_data(data):
    """
    Clean the data by:
    1. Replacing infinite values with Nan.
    2. Dropping rows with missing essential columns.
    3. Removing rows with zero values in spesific columns.
    """

    # replace infinite values with Nan
    data.replace([np.inf, -np.inf], np.nan, inplace = True)
    
    # drop rows with Nan values in required columns
    required_cols = ['city', 'price']
    data.dropna(subset=required_cols, inplace = True)

    # Removing rows with zero values in spesific columns.
    zero_cols = ['price', 'beds', 'sq__ft']
    data[zero_cols] = data[zero_cols].replace(0, np.nan)
    data.dropna(subset = zero_cols, inplace = True)

def create_report(data):
    # create report file with the following fields: city, avg price per city and total price per city 
    try:
        required_columns = ['city', 'price']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"The {col} column is missing in the given data.")
        
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
    
def create_additional_report(data):
    # create additional report file with the following fields:
    # city, avg beds number per city, avg square meter price,
    # first sale date per city and last sale date per city
    try:
        required_columns = ['city', 'beds', 'price', 'sale_date']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"The {col} column is missing in the given data.")
            
        # add new column for square meters
        if 'sq__ft' not in data.columns:
                raise ValueError(f"The 'sq__ft' column is missing in the given data.")
        
        SQ_M_TO_SQ_FT = 10.7639104
        data['sq__m'] = data['sq__ft'] / SQ_M_TO_SQ_FT
        data['price_per_sq__m'] = data['price'] / data['sq__m']

        additional_report = data.groupby('city').agg(
            avg_beds_number_per_city = ("beds", "mean"),
            avg_square_m_price = ("price_per_sq__m", "mean"),
            first_sale_date_per_city = ("sale_date", "min"),
            last_sale_date_per_city = ("sale_date", "max")
        ).reset_index()

        # save the report file
        additional_report_file_name = "additional_report.csv"
        additional_report.to_csv(additional_report_file_name, index = False)
        print(f"{additional_report_file_name} file has been successfully created.")

    except Exception as e:
        print(f"Error while creating the additional report file: {e}")

def main():
    file_name = "Sacramentorealestatetransactions (1).csv"

    data = load_csv_file(file_name)

    if data is not None:
        clean_data(data)
        create_report(data)
        create_additional_report(data)


if __name__ == "__main__":
    main()