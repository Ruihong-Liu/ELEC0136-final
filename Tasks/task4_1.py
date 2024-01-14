from task3_2 import plot_stock_data
from task3_1 import reconstucted_data,load_MongoDB_stock,filter_stock_data
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm
# save work in future
def data_load_filter_reconstruct():
    # load stock data from MongoDB
    stock_price=load_MongoDB_stock()
    #filter stock data from 2019-04-01 to 2023-03-31
    Filtered_data=filter_stock_data(stock_price)
    #reconstruct the data
    data=reconstucted_data(Filtered_data)
    return data
data=data_load_filter_reconstruct
print(data)

"""
def trend_analysis_30days(data,days=30):
    # Calculate the moving average
    data['Moving_Avg'] = data['Volume'].rolling(window=days).mean()
    # Plotting the Volume and its Moving Average
    plt.figure(figsize=(10, 6))
    plt.plot(data['Volume'], label='Volume')
    plt.plot(data['Moving_Avg'], label='30-Day Moving Average', color='red')
    plt.legend()
    plt.show()
trend_analysis_30days(data)



"""


