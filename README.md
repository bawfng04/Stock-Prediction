
# Stock Price Prediction

This project is a web application that uses a Long Short-Term Memory (LSTM) model to predict the stock price of companies using historical data. The application allows users to select one or more companies, specify the number of days to consider for the prediction, and displays the predicted closing price as well as a candlestick chart and a line chart for the selected companies.

## Features

1. **Company Selection**: The application provides a dropdown menu to select one or more companies from the S&P 500 index.
2. **Date Range Selection**: Users can specify the number of days to consider for the prediction, ranging from 1 to 3650 (approximately 10 years).
3. **Prediction and Visualization**: The application runs the LSTM model for the selected companies and displays the predicted closing price, a candlestick chart, and a line chart for the close price comparison.

## Screenshots
![image](https://github.com/user-attachments/assets/bb742eae-c2cf-4b08-87db-c9b5dbb9340e)
![image](https://github.com/user-attachments/assets/ddb5353a-197e-4e48-b974-85e3b81f2157)
![image](https://github.com/user-attachments/assets/84d297b9-e3be-441e-938e-86aa595bacd2)


## Prerequisites

- Python 3.x
- Pandas
- Yfinance
- Plotly
- Keras
- Scikit-learn
- Streamlit

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/stock-price-prediction.git
```

2. Navigate to the project directory:

```
cd stock-price-prediction
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:

```
streamlit run host.py
```

2. The application will open in your default web browser.
3. Select one or more companies from the dropdown menu.
4. Choose the number of days to consider for the prediction.
5. Click the "Run Predictions" button to see the results.

## File Structure

- `stockPrediction.py`: This Python script downloads the stock data, prepares the data for the LSTM model, builds and trains the model, and makes predictions.
- `host.py`: This Streamlit application provides the user interface, allows the user to select companies and the number of days, and displays the predictions and visualizations.
- `prediction_result.txt`: This file stores the predicted closing price for the selected companies.
- `fetched_data.csv`: This file stores the historical stock data for the selected companies.
