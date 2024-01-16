from task3_1 import load_MongoDB_stock,filter_stock_data,missing_check,check_holidays_weekend,extract_msft_relevance
from task3_1 import none_data_check,reconstucted_data,news_data_clean,load_MongoDB_news
from task3_2 import plot_stock_data,plot_volume_time
from task3_3 import normalize_data,pca

# load stock data from MongoDB
stock_price=load_MongoDB_stock()

#filter stock data from 2019-04-01 to 2023-03-31
Filtered_data=filter_stock_data(stock_price)

#check if there is any missing dates
miss_date=missing_check(Filtered_data)

#check if missing dates are weekend or USA public holiday
miss_weekdays=check_holidays_weekend(miss_date)

#check if there is any none data
none_data_check(Filtered_data)

#reconstruct the data
reconstucted=reconstucted_data(Filtered_data)
#check if there is any missing dates in constructed data
Reconstruct_days=missing_check(reconstucted)

#plot the origional data
plot_stock_data(Filtered_data,path='images/Task 3.1 Stock Price Data.png')
#plot the reconstructed data
plot_stock_data(reconstucted,path='images/Task 3.1 Reconstructed Stock Price Data.png')
#plot the volume data
plot_volume_time(Filtered_data,path='images/Task 3.1 Volume Data.png')
#plot the volume data of reconstructed data
plot_volume_time(reconstucted,path='images/Task 3.1 Reconstructed Volume Data.png')
#normalize the data
data_norm_ori=normalize_data(Filtered_data)
#normalize the reconstructed data
data_norm_recon=normalize_data(reconstucted)
#pca analysis normalized data
pca(data_norm_ori)
#pca analysis normalized reconstructed data
pca(data_norm_recon)
# for later task usage
def load_news_data_clean():
    #load news data from MongoDB
    news_df=load_MongoDB_news()
    #clean the news data
    clean_df=news_data_clean(news_df)
    #extract msft relevance score
    clean_df['msft_relevance_score'] = extract_msft_relevance(clean_df['ticker_sentiment'])
    print(clean_df)
    return news_df,clean_df
# load news data
news_df,clean_df=load_news_data_clean()
print(clean_df)