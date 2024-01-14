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

#plot the boxplot of price
def plot_price_boxplot(filtered_data,path):
    plt.figure(figsize=(10, 6))
    plt.boxplot([filtered_data['Open'], filtered_data['High'], filtered_data['Low'], filtered_data['Close']],
                labels=['Open', 'High', 'Low', 'Close'])
    plt.title('Boxplot for Open, High, Low, and Close Prices')
    plt.ylabel('Price')
    plt.savefig(path)

#plot the qq plot of close price
def qq_plot(filtered_data,path):
    plt.figure(figsize=(6, 6))
    stats.probplot(filtered_data['Close'], dist="norm", plot=plt)
    plt.title('Q-Q Plot of Close')
    plt.ylabel('Quantiles of Close')
    plt.xlabel('Theoretical Quantiles')
    plt.savefig(path)

#plot the scatter plot of volume and close price
def scatter_plot_volume_close(data,path):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Volume'], data['Close'], alpha=0.3, color='red', label='Volume vs. Close')
    plt.title('Scatter Plot of Volume and Close Price')
    plt.xlabel('Volume')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.legend()
    plt.savefig(path)