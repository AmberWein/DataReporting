import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load data
report = pd.read_csv("report.csv")
additional_report = pd.read_csv("additional_report.csv")

def plot_bar_chart(data, title, y_label, colors):
    # plots a bar chart for given data
    plt.figure(figsize = (8,5))

    # check if data is a dictionary
    if isinstance(data, dict):
        keys = list(map(str, data.keys()))
        values = list(data.values())
    else:
        keys = list(map(str, data.index))
        values = list(data.values.flatten())

    plt.bar(keys, values, color = colors)
    plt.title(title, fontsize = 14)
    plt.ylabel(y_label, fontsize = 12)
    plt.xticks(fontsize = 10)

    plt.show()

def plot_scatter(data):
    # plots a scatter for average price per square meters across cities
    plt.figure(figsize = (8,5))

    # normalize values for color mapping
    norm = ((data["avg_square_m_price"] - data["avg_square_m_price"].min()) /
                (data["avg_square_m_price"].max() - data["avg_square_m_price"].min()))
    colors = plt.cm.coolwarm(norm)

    plt.scatter(data['city'], data["avg_square_m_price"], c = colors, edgecolors = "black", cmap="coolwarm")

    plt.axhline(y = 4131.775933905455, color = "green", linestyle = "dashed", label = "Penryn")
    plt.axhline(y = 3.70, color = "blue", linestyle = "dashed", label = "Sloughhouse")

    plt.xticks(rotation = 90, fontsize = 10)
    plt.title("Average price per square meter across cities", fontsize = 14)
    plt.ylabel("Average price per m²", fontsize = 12)
    plt.legend()

    plt.show()

def plot_sales_distribution(data):
    # convert 'first_sale_date_per_city' column to datetime
    data['first_sale_date_per_city'] = pd.to_datetime(data['first_sale_date_per_city'], errors = "coerce" )
    data['first_sale_date_per_city'] = data['first_sale_date_per_city'].dt.strftime('%b %d')
    
    # count for each date the number of sales
    sales_count = data['first_sale_date_per_city'].value_counts().sort_index()

    cmap = plt.get_cmap("Blues")
    colors = cmap(np.linspace(0.4, 1, len(sales_count))) 

    # plots a bar chart for the distribution of sale dates
    plt.figure(figsize = (8,5))
    plt.bar(sales_count.index, sales_count.values, color = colors)

    plt.title("Distribution of sale dates", fontsize = 14)
    plt.ylabel("Sale date", fontsize = 12)
    plt.ylabel("Number of sales", fontsize = 12)
    plt.xticks(fontsize = 12)

    plt.show()

beds_data = {"Granite Bay": 4.67, "West Sacramento": 0.67, "Most cities": 3}
plot_bar_chart(beds_data, "Average beds per city", "Average bed count", ["green", "red", "blue"])

plot_scatter(additional_report)

plot_sales_distribution(additional_report)
