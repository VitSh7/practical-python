# report.py
#
# Exercise 2.4

import fileparse


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    prices1 = fileparse.parse_csv("Data/prices.csv", types=[str, float], has_headers=False)
    prices = {}
    for p in prices1:
        prices[p[0]] = float(p[1])

    return prices


def calculate_gains(portfolio, prices):
    for stock in portfolio:
        if stock["name"] in prices:
            change = prices[stock["name"]] - stock["price"]
            stock["price"] = prices[stock["name"]]
            stock["gain"] = change * stock["shares"]


def print_table(table):
    print('{:^10s} {:^10s} {:^10s} {:^10s}'.format('Name', "Shares", "Price", "Gain"))
    print('{:^10s} {:^10s} {:^10s} {:^10s}'.format('------', "------", "------",
                                                   "------"))
    for row in table:
        print('{name:<10s} {shares:^10d} {price:^10.2f} {gain:^10.2f}'.format_map(row))


Portfolio = fileparse.parse_csv("Data/portfolio.csv", types=[str, int, float], has_headers=True)
Prices = read_prices("Data/prices.csv")
calculate_gains(Portfolio, Prices)

print_table(Portfolio)
