import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# plot the boxplot of price
def plot_OBV(df,path):
    # calculate OBV for close and volume
    obv = [0]
    for i in range(1, len(df)):
        if df['Close'].iloc[i] > df['Close'].iloc[i-1]:
            obv.append(obv[-1] + df['Volume'].iloc[i])
        elif df['Close'].iloc[i] < df['Close'].iloc[i-1]:
            obv.append(obv[-1] - df['Volume'].iloc[i])
        else:
            obv.append(obv[-1])
    df['OBV'] = obv

    # plot OBV
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['OBV'], label='OBV')
    plt.title('On-Balance Volume (OBV)')
    plt.xlabel('Date')
    plt.ylabel('OBV')
    plt.legend()
    plt.grid(True)
    plt.savefig(path)

def plot_A_D(df,path):
    # calculate A/D line
    flow_multiplier = ((df['Close'] - df['Low']) - (df['High'] - df['Close'])) / (df['High'] - df['Low'])
    ad_line = (flow_multiplier * df['Volume']).cumsum()

    # add A/D line to dataframe
    df['AD_Line'] = ad_line

    # plot A/D line
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['AD_Line'], label='Accumulation/Distribution Line')
    plt.title('Accumulation/Distribution Line')
    plt.xlabel('Date')
    plt.ylabel('Accumulation/Distribution')
    plt.legend()
    plt.grid(True)
    plt.savefig(path)

#plot the ADI of price
def plot_Average_Directional_Index(df, path):

    # calculate the directional movement
    flow_multiplier = ((df['Close'] - df['Low']) - (df['High'] - df['Close'])) / (df['High'] - df['Low'])
    ad_line = (flow_multiplier * df['Volume']).cumsum()

    # add A/D line to dataframe
    df['AD_Line'] = ad_line

    # plot A/D line
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['AD_Line'], label='Accumulation/Distribution Line')
    plt.title('Accumulation/Distribution Line')
    plt.xlabel('Date')
    plt.ylabel('Accumulation/Distribution')
    plt.legend()
    plt.grid(True)
    plt.savefig(path)

def plot_Aroon_Indicator(df,path):
    N = 30
    # calculate Aroon Up and Down
    df['Aroon_Up'] = df['High'].rolling(window=N, min_periods=0).apply(lambda x: float(np.argmax(x) + 1) / N * 100, raw=True)
    df['Aroon_Down'] = df['Low'].rolling(window=N, min_periods=0).apply(lambda x: float(np.argmin(x) + 1) / N * 100, raw=True)

    # plot Aroon Up and Down
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Aroon_Up'], label='Aroon Up')
    plt.plot(df.index, df['Aroon_Down'], label='Aroon Down')
    plt.title('Aroon Indicator')
    plt.xlabel('Date')
    plt.ylabel('Aroon')
    plt.legend()
    plt.grid(True)
    plt.savefig(path)

def plot_MACD(df,path):
    # calculate MACD
    df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['EMA26'] = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD_Line'] = df['EMA12'] - df['EMA26']
    df['Signal_Line'] = df['MACD_Line'].ewm(span=9, adjust=False).mean()
    df['MACD_Histogram'] = df['MACD_Line'] - df['Signal_Line']

    # plot MACD
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.title('Stock Close Price')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(df.index, df['MACD_Line'], label='MACD Line')
    plt.plot(df.index, df['Signal_Line'], label='Signal Line')
    plt.bar(df.index, df['MACD_Histogram'], label='Histogram', color='grey')
    plt.title('Moving Average Convergence Divergence (MACD)')
    plt.legend()
    plt.savefig(path)

def plot_Relative_Strength_Index(df,path):
    # calculate difference in price from previous day
    delta = df['Close'].diff()

    # calculate gain and loss
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # calculate average gain and loss
    average_gain = gain.rolling(window=14, min_periods=14).mean()
    average_loss = loss.rolling(window=14, min_periods=14).mean()

    # calculate relative strength index
    rs = average_gain / average_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # plot RSI
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['RSI'], label='RSI')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid(True)
    plt.savefig(path)

def plot_Stochastic_Oscillator(df,path):
    N = 14  # Stochastic Oscillator parameter
    # calculate Stochastic Oscillator
    low_min = df['Low'].rolling(window=N).min()
    high_max = df['High'].rolling(window=N).max()
    df['%K'] = (df['Close'] - low_min) * 100 / (high_max - low_min)

    # calculate Moving Average of %K
    df['%D'] = df['%K'].rolling(window=3).mean()

    # plot Stochastic Oscillator
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['%K'], label='%K')
    plt.plot(df.index, df['%D'], label='%D')
    plt.title('Stochastic Oscillator')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.axhline(80, color='red', linestyle='--')
    plt.axhline(20, color='green', linestyle='--')
    plt.legend()
    plt.grid(True)
    plt.savefig(path)