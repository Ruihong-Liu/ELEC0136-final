from pymongo import MongoClient
from datetime import datetime
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd
import holidays

# function used to load stock data from MongoDB
def load_MongoDB_stock():
    # connected to the MongoDB server and chose the collection and database
    client = MongoClient("mongodb+srv://sui1223:Lrh118828769@cluster0.4axd2vy.mongodb.net/?retryWrites=true&w=majority")
    db = client["StockPrice"]
    collection = db["Microsoft"]
    # save the data as a list# save the data from MongoDB
    stock = collection.find()
    stock_price={}
    for price in stock:
        stock_price=price
    return stock_price

# function used to load news data from MongoDB
def load_MongoDB_news():
    # connected to the MongoDB server and chose the collection and database
    client = MongoClient("mongodb+srv://sui1223:Lrh118828769@cluster0.4axd2vy.mongodb.net/?retryWrites=true&w=majority")
    db=client["Newsdata"]
    collection=db["MicrosoftNews"]
    news=collection.find()
    # save the data as a list
    news_info = {}
    for info in news:
       news_info=info
    return news_info

# function used to filter the stock data from 2019-04-01 to 2023-03-31
def filter_stock_data(stock_price):
    # only take time series data from the dictionary
    time_series = stock_price.get("Time Series (Daily)", {})
    # Convert time series data to DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    # set date as index
    df.index = pd.to_datetime(df.index)
    df = df.apply(pd.to_numeric)
    # rename columns
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    # sort data by time
    df_sorted = df.sort_index()
    # Filter the data for outliers
    start_date = '2019-04-01'
    end_date = '2023-03-31'
    filtered_data = df_sorted.loc[start_date:end_date]
    return filtered_data
# 
def news_data_clean(news_info):
    # get feed only from the dictionary
    news_info_feed = news_info.get("feed", {})
    news_info_feed = pd.DataFrame(news_info_feed)
    column_names = news_info_feed.columns
    columns_needed=['title',"url","time_published",'summary','overall_sentiment_score','ticker_sentiment']
    clean_df = pd.DataFrame()
    for column in columns_needed:
        clean_df[column] = news_info_feed[column]
    clean_df.set_index("time_published", inplace=True)
    clean_df.index = pd.to_datetime(clean_df.index)
    clean_df['ticker_sentiment']
    return clean_df

def extract_msft_relevance(ticker_sentiment):
    msft_relevance_scores = []
    for row in ticker_sentiment:
        msft_score = next((item['relevance_score'] for item in row if item['ticker'] == 'MSFT'), None)
        msft_relevance_scores.append(msft_score)
    return msft_relevance_scores


# function used to check if there is any missing data
def missing_check(Filtered_data):
    # creat a full date list from 2019-04-01 to 2023-03-31
    start_date = '2019-04-01'
    end_date = '2023-03-31'
    date_range = pd.date_range(end=end_date,start=start_date,freq='D')
    # compare the full date list with the date in datafram
    missing_dates = date_range.difference(Filtered_data.index)
    if len(missing_dates) == 0:
        print("There is no missing date")
    return missing_dates

# if missing data is weekend or USA public holiday
def check_holidays_weekend(miss_date):
    non_trading_days = []
    # request USA public holidays
    us_holidays= holidays.UnitedStates(years=[2019, 2020, 2021, 2022, 2023])
    us_holidays = pd.to_datetime([i[0] for i in us_holidays.items()])
    # check if the missing date is a USA public holiday
    for date in miss_date:
        if date.weekday() <5 and date not in us_holidays:  # If it's not weekend or holiday
            non_trading_days.append(date)
    return non_trading_days

# check if there is any None value in the dataframe
def none_data_check(Filtered_data):
    # check if there is any None value in the dataframe
    if Filtered_data.isnull().values.any():
        print("There is None value in the dataframe")
    else:
        print("There is no None value in the dataframe")

# reconstuct the dataframe with linear interpolation
def reconstucted_data(filtered_data):
    # interpolate to fill the missing data
    resampled_data = filtered_data.resample('D').asfreq()
    interpolated_data = resampled_data.interpolate(method='linear')
    return interpolated_data

