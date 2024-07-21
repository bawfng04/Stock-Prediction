import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import subprocess
import os
#result



# streamlit run host.py

# test
# print("---------ALL-----------")
# for i, t in enumerate(table):
#     print(f"Table {i}:")
#     print(t.head())
#     print("\n")

# dfT = table[1]
# dataT = dfT['Date']
# print(dataT)
# selectTest = st.selectbox('Select Date', dataT)
# print("---------TABLE 1-----------")
# dfT = table[1]
# print(dfT.head())



#title
st.title('Stock Price Prediction')
#description
st.write('A LSTM model to predict the stock price of companies using historical data.')

################## select company ##################
#get tickers
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
table = pd.read_html(url) #read html tables
df = table[0]
companyName = df['Security'].tolist() #company name
companySymbol = df['Symbol'].tolist() #company symbol
maps = dict(zip(companyName, companySymbol)) #[Apple, AAPL]

#streamlit <select>
stock_name = st.selectbox('Select Company', companyName)
#maps

if stock_name:
    selectedCompany = maps[stock_name]
    st.write(selectedCompany)
# =>  selectedCompany

################## select date ##################
# selectedBeginDay = st.date_input('Select Begin Date', pd.to_datetime('2024-01-01'))
# selectedEndDay = st.date_input('Select End Date', pd.to_datetime('2024-12-31'))

selectedDays = st.slider('Select number of rollback days', min_value=1, max_value=3650, value=30, step=1)
st.write(f'You selected {selectedDays} days')

#combine 2 files
if st.button('Run'):
    #waiting for the model
    with st.empty():
        st.write('Running the model...')
        subprocess.run(["python", "stockPrediction.py", selectedCompany, str(selectedDays)], check=True)
        st.write("")

    #display result
    st.write(f"Stock Prediction for {stock_name} is completed.")
    with open('prediction_result.txt', 'r') as file:
        prediction_result = file.read()
    st.write(f"Predicted closing price of { stock_name } is: { prediction_result }")
    #display fetched data
    with open('fetched_data.csv', 'r') as file:
        data = pd.read_csv(file)
    st.write(data.head()) #display first 5 rows
    #st.write(data); #display all data