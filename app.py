from flask import Flask, render_template, request, flash, url_for
import csv

from datetime import datetime
from dataFetcher import getStockData
from graphGenerator import generate_graph
from timeSeriesFunctions import getTimeSeriesFunction
from main import preprocess_data
import os
from time import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

def get_stock_symbols():
    stock_symbols = []
    with open('stocks.csv', newline='') as csvfile:
        stockreader = csv.DictReader(csvfile)
        for row in stockreader:
            stock_symbols.append(row['Symbol'])
    return stock_symbols

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_symbols = get_stock_symbols()
    graph_url = None  # Initialize graph_url to None

    if request.method == 'POST':
        symbol = request.form.get('symbol')
        chart_type = request.form.get('chart_type')
        time_series = request.form.get('time_series')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        api_function = {
            "intraday": "TIME_SERIES_INTRADAY",
            "daily": "TIME_SERIES_DAILY",
            "weekly": "TIME_SERIES_WEEKLY",
            "monthly": "TIME_SERIES_MONTHLY"
        }.get(time_series, "TIME_SERIES_DAILY")

        api_key = "V6BVQP0SPVJAVA6X"
        raw_data = getStockData(symbol, api_function, api_key)

        if not raw_data:
            flash(f"Failed to fetch data for symbol: {symbol}")
        else:
            filtered_data = preprocess_data(raw_data, start_date, end_date)
            if not filtered_data:
                flash("No data available for the selected date range.")
            else:
                graph_filename = generate_graph(filtered_data, chart_type, start_date, end_date, symbol)
            if graph_filename:  # Check if a filename was returned
                graph_url = url_for('static', filename=graph_filename) + f"?{time()}"


    return render_template('index.html', stock_symbols=stock_symbols, graph_url=graph_url)


if __name__ == '__main__':
    app.run(debug=True)