import time
import csv
from dataclasses import dataclass
from pprint import pprint

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
costs = []
for i in stocks:
    costs.append(i.cost)
rets = []
for i in stocks:
    rets.append(i.cost * i.ret)
stocks_names = []
for i in stocks:
    stocks_names.append(i.name)


def solve_bruteforce(profits, weights, capacity):
    return solve_bruteforce_recursive(profits, weights, capacity, 0)


def solve_bruteforce_recursive(profits, weights, capacity, current_index):
    if capacity <= 0 or current_index >= len(profits):
        return 0

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + solve_bruteforce_recursive(
            profits, weights, capacity - weights[current_index], current_index + 1)

    profit2 = solve_bruteforce_recursive(profits, weights, capacity, current_index + 1)

    return max(profit1, profit2)


def solve_dynamic(profits, weights, capacity):
    table = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return solve_dynamic_recursive(table, profits, weights, capacity, 0)


def solve_dynamic_recursive(table, profits, weights, capacity, current_index):
    if capacity <= 0 or current_index >= len(profits):
        return 0

    if table[current_index][capacity] != -1:
        return table[current_index][capacity]

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + solve_dynamic_recursive(
            table, profits, weights, capacity - weights[current_index], current_index + 1)

    profit2 = solve_dynamic_recursive(table, profits, weights, capacity, current_index + 1)

    table[current_index][capacity] = max(profit1, profit2)
    return table[current_index][capacity]


def solve_bottomup(profits, weights, capacity):
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
    total_profit = table[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        if total_profit != table[i - 1][capacity]:
            print(f'{str(stocks[i].name)} ', end='\n')
            capacity -= weights[i]
            total_profit -= profits[i]

    if total_profit != 0:
        print(f'{str(stocks[0].name)} ', end='')
    print()


# print(solve_bruteforce(rets, costs, max_investment))
# print(solve_dynamic(rets, costs, max_investment) / 100)
print(solve_bottomup(rets, costs, max_investment) / 100)

print(time.time() - start_time, "seconds")
