import pandas as pd
import numpy as np
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR

def train_ARMA_model(df,path):
    # 使用过去5天的数据来预测未来30天
    n_past = 60
    n_future = 30

    # 提取最初的历史数据（最后五天）
    initial_history = df['Close'][-n_past:].tolist()

    # 存储历史数据和预测结果
    combined_history = initial_history.copy()
    predictions = []

    # 获取最后一个已知交易日的日期
    last_date = df.index[-1]

    # 递归地进行预测
    for t in range(n_future):
        # 建立并拟合模型
        model = ARIMA(combined_history, order=(1, 0, 1))  # 参数可能需要根据您的数据进行调整
        model_fit = model.fit()

        # 预测下一天的价格
        output = model_fit.forecast()
        yhat = output[0]

        # 计算下一个预测日期，跳过周末和其他非交易日
        next_date = last_date + pd.DateOffset(days=1)
        while next_date.weekday() > 4:  # 0-4对应周一至周五
            next_date += pd.DateOffset(days=1)

        # 更新最后一个交易日的日期
        last_date = next_date

        # 将预测值添加到历史数据中（不影响原始数据集）
        combined_history.append(yhat)
        predictions.append((next_date, yhat))
    forecast_df = pd.DataFrame(predictions, columns=['Date', 'Predicted'])
    forecast_df.set_index('Date', inplace=True)
        # 绘制预测值与实际值
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Historical Close Price')

    # 绘制预测数据
    plt.plot(forecast_df['Predicted'], label='Predicted Close Price', color='orange')

    # 添加标题和图例
    plt.title('Stock Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()

    # 显示图表
    plt.savefig(path)
    return predictions
