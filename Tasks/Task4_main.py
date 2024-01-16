from task4_1 import trend_analysis_30days,data_load_filter_reconstruct,seasonal_analysis,noise_analysis1,noise_analysis2,plot_price_boxplot,qq_plot,scatter_plot_volume_close
from task4_1 import calculate_slopes,remove_close_dates,calculate_high_low_difference,get_news_titles_around_dates,plot_hypothesis_testing
from Task4_2 import plot_OBV,plot_A_D,plot_Average_Directional_Index,plot_Aroon_Indicator,plot_MACD,plot_Relative_Strength_Index,plot_Stochastic_Oscillator
from Task3_main import load_news_data_clean

# load data
data = data_load_filter_reconstruct()

# plot the trend analysis for 90 days
trend_analysis_30days(data,90,path='images/Task 4.1 trend_90days.png')
# plot the seasonal analysis
seasonal_analysis(data,path='images/Task 4.1 seasonal.png')
# plot the noise analysis
noise_analysis1(data,path='images/Task 4.1 noise1 ARIMA.png')
noise_analysis2(data,path='images/Task 4.1 noise2 resample.png')
#plot the boxplot of price
plot_price_boxplot(data,path='images/Task 4.1 Boxplot for Open, High, Low, and Close Prices.png')
#plot the qq plot of price
qq_plot(data,path='images/Task 4.1 Q-Q Plot of Close.png')

#plot the scatter plot of volume and close price of origional data
scatter_plot_volume_close(data,path='images/Task 4.1 Scatter Plot of Volume and Close.png')
# calculate the slope of continuous 10 days data using close price
slopes = calculate_slopes(data, window_size=10)
# sort the slopes and find the largest 10 slopes
sorted_slopes = slopes.sort_values(ascending=False)
sorted_slopes= remove_close_dates(sorted_slopes,)
# calculate the difference between the highest and lowest price of each day
High_Low_diff=calculate_high_low_difference(data)
sorted_diff = data.sort_values(by='High_Low_Difference', ascending=False)

# load news data
news_df,clean_df=load_news_data_clean()
print(sorted_slopes.index[:10])
title_slop=get_news_titles_around_dates(clean_df,dates=sorted_slopes.index[:10])
print(title_slop)
title_diff=get_news_titles_around_dates(clean_df,dates=sorted_diff.index[:10])
print(title_diff)

# plot the hypothesis testing
plot_hypothesis_testing(data,path='images/Task 4.1 hypothesis testing.png')

# plot obv
plot_OBV(data,path='images/Task 4.2 OBV.png')
plot_A_D(data,path='images/Task 4.2 A_D.png')

#plot the ADI of price
plot_Average_Directional_Index(data,path='images/Task 4.2 ADI.png')

# plot the arroon indicator
plot_Aroon_Indicator(data,path='images/Task 4.2 Aroon Indicator.png')

# plot the MACD
plot_MACD(data,path='images/Task 4.2 MACD.png')

# plot the RSI
plot_Relative_Strength_Index(data,path='images/Task 4.2 RSI.png')

# plot the Stochastic Oscillator
plot_Stochastic_Oscillator(data,path='images/Task 4.2 Stochastic Oscillator.png')