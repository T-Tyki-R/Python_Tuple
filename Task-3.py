# Python Loops and Tuples in Analytical Applications

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def stock_data_average(data_list):
    data_sum = 0
    counter = 0
    for i in data_list:
        name, date, revenue = i
        if name == "AAPL":
            data_sum += revenue
            counter += 1
    return data_sum / counter

print(f"The average for AAPL is: {stock_data_average(stock_data)}")