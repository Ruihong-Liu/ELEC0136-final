"""
Task 1.1 and task 1.2 
task 1.1 request stock data from Web API
task 1.2 request news data from Web API
"""
from Tasks.task1_1 import aqu_stock_data
from Tasks.task1_2 import get_news_data
# function of request data
def request_data():
    #API keys
    api_key="NN2SRNCT5M2N98WP"
    #api_key='TVQPPAU7D3SY0U1R'
    ##chose the company symbol
    symbol  =   "MSFT"
    ##request data
    stock_data = aqu_stock_data(symbol,api_key)
    news_data = get_news_data(symbol,api_key)
    return stock_data,news_data
req_stock_data,req_news_data=request_data()
"""
Task 2.1 and task 2.2
task 2.1 upload stock data and newsdata to MongoDB
task 2.2 creat CURD functions for MongoDB
"""
from Tasks.Task2_1 import up_mongoDB
from Tasks.task2_2 import Create,Read,Update,Delete
# upload stock data and news data to MongoDB
up_mongoDB(req_stock_data,req_news_data)
# creat CURD functions for MongoDB
#Create()
#Read()
#Update()
#Delete()
"""
Task 3.1 and task 3.2 task 3.3
task 3.1 load stock data and news data from MongoDB and filter the data
task 3.2 visualize the data
task 3.3 transform the data
"""
from Tasks.task3_1 import load_MongoDB_stock,load_MongoDB_news,filter_stock_data,news_data_clean,extract_msft_relevance
from Tasks.task3_1 import missing_check,check_holidays_weekend,none_data_check,reconstucted_data
# load stock data and news data from MongoDB
ori_stock_data=load_MongoDB_stock()
ori_news_data=load_MongoDB_news()
# filter the data
filtered_stock_data_train=filter_stock_data(ori_stock_data,"2019-04-01","2023-03-31")
filtered_stock_data_test=filter_stock_data(ori_stock_data,"2023-04-01","2023-4-30")
# filter the news data
clean_news_data=news_data_clean(ori_news_data)
clean_news_data['msft_relevance_score']=extract_msft_relevance(clean_news_data['ticker_sentiment'])
# missing check
missing_days=missing_check(filtered_stock_data_train)
missing_days_final=check_holidays_weekend(missing_days)
print("the missing days which is not recognised as weekends and public holidays are",missing_days_final)
none_data_check(filtered_stock_data_train)
# reconstruct the data
reconstructed_stock_data=reconstucted_data(filtered_stock_data_train)
none_data_check(reconstructed_stock_data)
from Tasks.task3_2 import plot_stock_data,plot_volume_time
# plot the stock data
plot_stock_data(reconstructed_stock_data,path="images/Task 3.1 visualized stock data price.png")
# plot the volume data
plot_volume_time(reconstructed_stock_data,path="images/Task 3.1 visualized stock data volume.png")
from Tasks.task3_3 import normalize_data,pca
# normalize the data
normalized_stock_data=normalize_data(reconstructed_stock_data)
# pca analysis
n_components=pca(normalized_stock_data)
"""
task 4.1 and task 4.2
task 4.1 analyse the stock data
task 4.2 calculate the indecators of the stock data
"""
from Tasks.task4_1 import trend_analysis_30days
# plot the trend analysis for n days
trend_analysis_30days(reconstructed_stock_data,30,path="images/Task 4.1 trend analysis yearly.png")
from Tasks.task4_1 import seasonal_analysis
# plot the seasonal analysis
seasonal_analysis(reconstructed_stock_data,path="images/Task 4.1 seasonal analysis.png")
from Tasks.task4_1 import noise_analysis1,noise_analysis2
# plot the noise analysis using ARIMA
noise_analysis1(reconstructed_stock_data,path="images/Task 4.1 noise analysis ARIMA.png")
# plot the noise analysis using resample
noise_analysis2(reconstructed_stock_data,path="images/Task 4.1 noise analysis resample.png")
from Tasks.task4_1 import plot_price_boxplot
# plot the boxplot of price
plot_price_boxplot(reconstructed_stock_data,path="images/Task 4.1 boxplot of price.png")
from Tasks.task4_1 import qq_plot
# plot the qq plot of close price
qq_plot(reconstructed_stock_data,path="images/Task 4.1 qq plot of close price.png")
from Tasks.task4_1 import scatter_plot_volume_close
# plot the scatter plot of volume and close price
scatter_plot_volume_close(reconstructed_stock_data,path="images/Task 4.1 scatter plot of volume and close price.png")
from Tasks.task4_1 import plot_hypothesis_testing
# plot the hypothesis testing
plot_hypothesis_testing(reconstructed_stock_data,path="images/Task 4.1 hypothesis testing.png")
# link the news to the price data
from Tasks.task4_1 import calculate_slopes,remove_close_dates,calculate_high_low_difference,get_news_titles_around_dates
# calculate the slope of continuous 10 days data using close price
slopes = calculate_slopes(reconstructed_stock_data, window_size=10)
# sort the slopes and find the largest 10 slopes
sorted_slopes = slopes.sort_values(ascending=False)
sorted_slopes= remove_close_dates(sorted_slopes,)
# calculate the difference between the highest and lowest price of each day
High_Low_diff=calculate_high_low_difference(reconstructed_stock_data)
sorted_diff = reconstructed_stock_data.sort_values(by='High_Low_Difference', ascending=False)
# load news data
title_slop=get_news_titles_around_dates(clean_news_data,dates=sorted_slopes.index[:10])
print("the relevant news about Microsof which afftects the most for a period of time",title_slop)
title_diff=get_news_titles_around_dates(clean_news_data,dates=sorted_diff.index[:10])
print("the relevant news about Microsof which afftects the most for a day",title_diff)
# task 4.2 plot indecators
from Tasks.Task4_2 import plot_OBV
# plot obv
OBV_df=plot_OBV(reconstructed_stock_data,path="images/Task 4.2 OBV.png")
from Tasks.Task4_2 import plot_A_D
# plot A_D
plot_A_D(reconstructed_stock_data,path="images/Task 4.2 A_D.png")
from Tasks.Task4_2 import plot_Average_Directional_Index
# plot ADI
plot_Average_Directional_Index(reconstructed_stock_data,path="images/Task 4.2 ADI.png")
from Tasks.Task4_2 import plot_Aroon_Indicator
# plot Aroon Indicator
plot_Aroon_Indicator(reconstructed_stock_data,path="images/Task 4.2 Aroon Indicator.png")
from Tasks.Task4_2 import plot_MACD
# plot MACD
MACD_df=plot_MACD(OBV_df,path="images/Task 4.2 MACD.png")
from Tasks.Task4_2 import plot_Relative_Strength_Index
print("the data now has the colum",MACD_df.columns)
# plot RSI
plot_Relative_Strength_Index(reconstructed_stock_data,path="images/Task 4.2 RSI.png")
from Tasks.Task4_2 import plot_Stochastic_Oscillator
# plot Stochastic Oscillator
plot_Stochastic_Oscillator(reconstructed_stock_data,path="images/Task 4.2 Stochastic Oscillator.png")
"""
Task 5.1 and task 5.2
task 5.1 forcasting using LSTM with only close price data
task 5.2 forcasting using LSTM with OBV data and MACD data and predicte close price for next 30 days
"""
from Tasks.task5_1_LSTM import Model_train_LSTM
# train LSTM model with n days data
predict1=Model_train_LSTM(OBV_df,filtered_stock_data_test["Close"],path="images/Task 5.1 LSTM.png",days=30)
from Tasks.task5_2_LSTM import Model_train_LSTM_with_OBV
# train LSTM model with n days data with external data
predict2=Model_train_LSTM_with_OBV(OBV_df,filtered_stock_data_test["Close"],path="images/Task 5.2 LSTM.png",days=30)
print(filtered_stock_data_test["Close"])
print(predict1)
from sklearn.metrics import r2_score
# calculate the r2 score for model 1
r_1 = r2_score(filtered_stock_data_test["Close"], predict1)
print("R-squared for the model task 5.1 is:", r_1)
# calculate the r2 score for model 2
r_2 = r2_score(filtered_stock_data_test["Close"], predict2)
print("R-squared for the model task 5.1 is:", r_2)
from sklearn.metrics import mean_squared_error
# calculate the mean square error for model 1
mse_1 = mean_squared_error(filtered_stock_data_test["Close"], predict1)
print("Mean Squared Error:", mse_1)
mse_2 = mean_squared_error(filtered_stock_data_test["Close"], predict1)
print("Mean Squared Error:", mse_2)
def joint_plot(df,predicted_df,path):
    import seaborn as sns
    import matplotlib.pyplot as plt
    actual_prices = df['Close']
    predicted_prices = predicted_df['Predicted']
    # plot jointplot
    sns.jointplot(x=actual_prices, y=predicted_prices, kind='scatter', marginal_kws=dict(bins=25, fill=True))
    plt.suptitle('joint plot of actual and predicted prices')
    plt.xlabel('actual prices')
    plt.ylabel('predicted prices')
    plt.savefig(path)
joint_plot(filtered_stock_data_test,predict1,path="images/Task 5.3 joint plot Model 1.png")
joint_plot(filtered_stock_data_test,predict2,path="images/Task 5.3 joint plot Model 2.png")




""""
Task 6 decision making
by using the gradient of the predicted price
positive gradient means the price will increase
negative gradient means the price will decrease
a threshold can be set to determine the decision
"""
import numpy as np
time = np.arange(1, len(predict1) + 1)
slope, intercept = np.polyfit(time,predict1, 1)
slope, intercept = np.polyfit(time,predict2, 1)
print("gradient of the predicted result is：", slope)
threshold = 0.01
if slope > threshold:
    print("buy more stocks, as price would increase")
if slope < -threshold:    
    print("sale some stocks, as price would decrease")
else:
    print("hlod it, as price would not change much")