from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from scipy import stats
import numpy as np
import pandas as pd
from datetime import timedelta
from scipy.stats import linregress
from scipy import stats
# plot the trend analysis for n days
def trend_analysis_30days(data,days,path):
    # Calculate the moving average
    data['Moving_Avg'] = data['Volume'].rolling(window=days).mean()
    # Plotting the Volume and its Moving Average
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['Moving_Avg'], label='30-Day Moving Average', color='red')
    plt.legend()
    plt.savefig(path)
# plot the seasonal analysis
def seasonal_analysis(data,path):
    # Decompose the time series
    decomposed = seasonal_decompose(data['Close'], model='additive', period=365)
    # Plotting the decomposed components
    decomposed.plot()
    plt.savefig(path)
# plot the noise analysis using ARIMA
def noise_analysis1(data,path):
    #noise analysis using ARIMA
    model = ARIMA(data['Close'], order=(5,1,0))
    model_fit = model.fit()
    # residuals
    residuals = model_fit.resid
    # plot residuals
    plt.figure(figsize=(10, 6))
    plt.plot(residuals)
    plt.title('ARIMA residuals')
    plt.savefig(path)
# plot the noise analysis using resample
def noise_analysis2(data,path):
    # resample monthly
    monthly_data = data['Close'].resample('M').mean()
    # plot monthly data
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data)
    plt.title('monthly sales Close data')
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

# calculate the slope of continuous 10 days data using close price
def calculate_slopes(df, window_size=10):
    # Calculate the slope of continuous 10 days data using close price
    def get_slope(y_values):
        x_values = np.arange(len(y_values))
        slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)
        return abs(slope)
    slopes = df['Close'].rolling(window=window_size).apply(get_slope, raw=True)
    return slopes

# remove the data points with close dates
def remove_close_dates(slopes, days_threshold=15):
    # Convert the index to datetime
    slopes.index = pd.to_datetime(slopes.index)
    
    # list of indexes to drop
    to_drop = []
    for i in range(len(slopes)):
        for j in range(i+1, len(slopes)):
            # calculate the difference between two dates
            date_diff = abs((slopes.index[i] - slopes.index[j]).days)
            # if the difference is less than 15 days
            if date_diff <= days_threshold:
                # keep the data point with larger slope
                smaller_slope_idx = i if slopes.iloc[i] < slopes.iloc[j] else j
                if smaller_slope_idx not in to_drop:
                    to_drop.append(smaller_slope_idx)

    # drop the data points
    slopes = slopes.drop(slopes.index[to_drop])
    return slopes
# calculate the difference between the highest and lowest price of each day
def calculate_high_low_difference(df):
    df['High_Low_Difference'] = (df['High'] - df['Low']).abs()
    return df

# get the news titles around the dates
def get_news_titles_around_dates(news_df, dates, days=5):
    news_titles = {}
    for date in dates:
        start_date = date - timedelta(days=days)
        end_date = date + timedelta(days=days)
        # find news within 5 days of the date
        mask = (news_df.index >= start_date) & (news_df.index <= end_date)
        relevant_news = news_df.loc[mask]
        # get the titles
        news_titles[date] = relevant_news['title'].tolist()
    return news_titles

def plot_hypothesis_testing(df,path):
    # z-score
    df['Z_Score'] = stats.zscore(df['Close'])
    outliers_z = df[(df['Z_Score'] > 3) | (df['Z_Score'] < -3)]

    # print("Outliers using Z-Score method:\n", outliers_z)
    print("Outliers using Z-Score method:\n", outliers_z)
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Z_Score'], label='Z-Score')
    plt.axhline(y=2.5, color='r', linestyle='--', label='Upper Threshold (2.5)')
    plt.axhline(y=-2.5, color='g', linestyle='--', label='Lower Threshold (-2.5)')
    plt.title('Z-Score of Close Prices')
    plt.xlabel('Date')
    plt.ylabel('Z-Score')
    plt.legend()
    plt.grid(True)
    plt.savefig(path)
