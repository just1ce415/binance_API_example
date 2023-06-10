import csv
from binance.client import Client

api_key = 'your_api_key'
api_secret = 'your_api_secret'

interval = '1h'  # Interval of collection (1d, 4h, 1h, etc.)
symbol = 'BTCUSDT'  # Symbol to collect data about

client = Client(api_key, api_secret)

# Get candlestick data
candles = client.get_klines(symbol=symbol, interval=interval)

# Define the CSV file path
csv_file = f'{symbol}_{interval}.csv'

# Save data to CSV
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time'])
    for candle in candles:
        writer.writerow(candle)

print(f'Data collected and saved to {csv_file}')
