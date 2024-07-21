import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM
import numpy as np

# Define constants for the script
STOCK_SYMBOL = 'AAPL'
DAYS_BACK = 5000

def download_stock_data(symbol, start_date, end_date):
    """Download stock data from Yahoo Finance."""
    data = yf.download(symbol, start=start_date, end=end_date, progress=False)
    data.reset_index(inplace=True)
    return data

def plot_candlestick_chart(data):
    """Plot a candlestick chart for the stock data."""
    figure = go.Figure(data=[go.Candlestick(x=data['Date'],
                                            open=data['Open'],
                                            high=data['High'],
                                            low=data['Low'],
                                            close=data['Close'])])
    figure.update_layout(title=f"{STOCK_SYMBOL} Stock Price Analysis", xaxis_rangeslider_visible=False)
    figure.show()

def prepare_data_for_model(data):
    """Prepare data for LSTM model."""
    x = data[['Open', 'High', 'Low', 'Volume']].to_numpy()
    y = data['Close'].to_numpy().reshape(-1, 1)
    return train_test_split(x, y, test_size=0.2, random_state=42)

def build_and_train_model(x_train, y_train):
    """Build and train LSTM model."""
    model = Sequential([
        LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 1)),
        LSTM(64, return_sequences=False),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=1, epochs=30)
    return model

def main():
    start_date = (date.today() - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
    end_date = date.today().strftime("%Y-%m-%d")

    data = download_stock_data(STOCK_SYMBOL, start_date, end_date)
    plot_candlestick_chart(data)

    print(data.corr()["Close"].sort_values(ascending=False))

    x_train, x_test, y_train, y_test = prepare_data_for_model(data)
    model = build_and_train_model(x_train, y_train)

    # Predict with a sample feature set
    features = np.array([[177.089996, 180.419998, 177.070007, 74919600]])
    print(model.predict(features))

if __name__ == "__main__":
    main()