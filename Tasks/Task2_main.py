from Task2_1 import up_mongoDB
from Task1_main import main1
#requests data useing task 1 code
stock_data,news_data=main1()
#upload data to MongoDB
up_mongoDB(stock_data,news_data)