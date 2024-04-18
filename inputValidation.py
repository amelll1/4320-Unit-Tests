import re

def validate_symbol(symbol):
    return re.match(r'^[A-Z]{1,7}$', symbol) is not None

def validate_chart_type(chart_type):
    return chart_type in ['1', '2']

def validate_time_series(time_series):
    return time_series in ['1', '2', '3', '4']

def validate_date(date_str):
    #Don't know if I need this fully
    return True  # Placeholder return value for now
