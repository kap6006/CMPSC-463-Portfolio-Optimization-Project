import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

stocks = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'LLY', 'UNH', 'V', 'JPM', 'WMT', 'XOM', 'MA', 'AVGO', 'JNJ', 'PG', 'ORCL', 'HD', 'ADBE', 'CVX', 'COST', 'MRK', 'KO', 'ABBV', 'CRM', 'BAC', 'PEP', 'ACN', 'MCD']

end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

data_list = []

for stock in stocks:
    df = yf.download(stock, start=start_date, end=end_date)
    df['Symbol'] = stock
    data_list.append(df)

master_data = pd.concat(data_list)

master_data.to_csv('master_data.csv')

print("Data for 5 years has been downloaded and saved to 'master_data.csv'.")