from task3_1 import filter_stock_data,load_MongoDB_stock
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
# load stock data from MongoDB
stock_price=load_MongoDB_stock()
#filter stock data from 2019-04-01 to 2023-03-31
Filtered_data=filter_stock_data(stock_price)
#plot the origional data with line of the best fit to show the trend
def plot_stock_data(filtered_data,path):
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['Open'], label='Open')
    plt.plot(filtered_data['Close'], label='Close')
    plt.plot(filtered_data['High'], label='High')
    plt.plot(filtered_data['Low'], label='Low')
    x = np.arange(len(filtered_data.index))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, filtered_data['Close'])
    best_fit_line = slope * x + intercept
    plt.plot(filtered_data.index, best_fit_line, color='red', label=f'Best Fit Line: y={slope:.2f}x+{intercept:.2f}')
    plt.grid(True)
    plt.title('Stock Price Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig(path)

#plot the volume data
def plot_volume_time(filtered_data,path):
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['Volume'], label='Volume')
    plt.grid(True)
    plt.title('Volume Data')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend()
    plt.savefig(path)

