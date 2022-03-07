import csv
from dataclasses import dataclass


@dataclass
class Stock:
    name: str
    cost: int
    ret: float


with open("data/dataset_light.csv", "r") as dataset:
    data_reader = csv.reader(dataset)
    next(data_reader, None)
    stocks = []
    for line in data_reader:
        name = line[0]
        cost = line[1]
        ret = line[2]

        stock = Stock(name, int(cost), float(ret))
        stocks.append(stock)

print(stocks)


def knapsack(w, wt, val, n):
    if n == 0 or w == 0:
        return 0
    if wt[n - 1] > w:
        return knapsack(w, wt, val, n-1)
    else:
        return max(val[n-1] + knapsack(w-wt[n-1], wt, val, n-1), knapsack(w, wt, val, n-1))


w = 500
n = len(stocks)
val = []
wt = []
for stock in stocks:
    val.append(stock.ret)
    wt.append(stock.cost)

print(knapsack(w, wt, val, n))
