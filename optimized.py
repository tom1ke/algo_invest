import time
import csv
from dataclasses import dataclass

start_time = time.time()


@dataclass
class Stock:
    name: str
    cost: int
    ret: float


with open("data/dataset2_Python+P7.csv", "r") as dataset:
    data_reader = csv.reader(dataset)
    next(data_reader, None)
    stocks = []
    for line in data_reader:
        name = line[0]
        cost = int(float(line[1]) * 100)
        ret = float(line[2]) / 100

        if cost > 0 and ret > 0:
            stock = Stock(name, cost, ret)
            stocks.append(stock)


n = len(stocks)
max_investment = 50000
costs = [i.cost for i in stocks]
rets = [i.cost * i.ret for i in stocks]


def solve_dynamic(profits, weights, capacity):
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    table = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    for i in range(n):
        table[i][0] = 0

    for c in range(capacity + 1):
        if weights[0] <= c:
            table[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + table[i - 1][c - weights[i]]
            profit2 = table[i - 1][c]
            table[i][c] = max(profit1, profit2)

    print_selected_stocks(table, profits, weights, capacity)
    return table[n - 1][capacity]


def print_selected_stocks(table, profits, weights, capacity):
    print("Need to buy: ", end='\n')
    investment_cost = 0
    total_profit = table[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        try:
            if total_profit != table[i - 1][capacity]:
                print(f'{str(stocks[i].name)} ', end='\n')
                investment_cost += weights[i]
                capacity -= weights[i]
                total_profit -= profits[i]
        except IndexError:
            break

    if total_profit != 0:
        print(f'{str(stocks[0].name)} ', end='')
        investment_cost += stocks[0].cost
    print()
    print(f'Cost : {investment_cost / 100}€')


print(f'Profit : {solve_dynamic(rets, costs, max_investment) / 100}€')

print(time.time() - start_time, "seconds")
