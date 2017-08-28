# dict min max

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


min_price = max(zip(prices.values(), prices.keys()))  # creates iterator

print min_price