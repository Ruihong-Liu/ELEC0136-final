from task5_1 import train_ARIMA_model,train_VAR_model
from task4_1 import data_load_filter_reconstruct
stock_data = data_load_filter_reconstruct()
predicted_series = train_ARIMA_model(stock_data,'images/Task5_1.png')
print(predicted_series)
predicted_series = train_VAR_model(stock_data,'images/Task5_2.png')
print(predicted_series)