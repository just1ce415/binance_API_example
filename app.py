from flask import Flask, render_template, jsonify
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)

@app.route('/candlestick/<string:symbol>/<string:interval>')
def display_candlestick(symbol, interval):
    # Read the candlestick data from the CSV file
    try:
        df = pd.read_csv(f'{symbol}_{interval}.csv')
    except Exception:
        return jsonify("File not found"), 404

    # Create a Plotly candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=df['Open Time'],
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])

    # Set chart layout
    fig.update_layout(title='Candlestick Chart',
                      xaxis_rangeslider_visible=False)

    # Convert the chart to JSON
    chart_json = fig.to_json()

    return render_template('candlestick.html', chart_json=chart_json)

@app.route('/piechart')
def display_piechart():
    # Sample market cap data for 10 symbols
    symbols = ['BTC', 'ETH', 'XRP', 'LTC', 'ADA', 'DOT', 'LINK', 'BCH', 'BNB', 'XLM']
    # Assuming we don't have such data for now, pick random market caps
    market_caps = [500, 400, 300, 200, 150, 120, 100, 90, 80, 70]

    # Create a Plotly pie chart
    fig = go.Figure(data=[go.Pie(labels=symbols, values=market_caps)])

    # Set chart layout
    fig.update_layout(title='Market Cap Pie Chart')

    # Convert the chart to JSON
    chart_json = fig.to_json()

    return render_template('piechart.html', chart_json=chart_json)
