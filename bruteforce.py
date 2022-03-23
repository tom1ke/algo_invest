import time
import csv
from dataclasses import dataclass

start_time = time.time()


@dataclass
class Stock:
    name: str
    cost: float
    ret: float


dataset0 = "data/dataset_light.csv"
dataset1 = "data/dataset1_Python+P7.csv"
dataset2 = "data/dataset2_Python+P7.csv"

with open(dataset0, "r") as dataset:
    data_reader = csv.reader(dataset)
    next(data_reader, None)
    stocks = []
    for line in data_reader:
        name = line[0]
        cost = float(line[1])
        ret = float(line[2]) / 100

        if cost > 0 and ret > 0:
            stock = Stock(name, cost, ret)
            stocks.append(stock)

n = len(stocks)
possible_combinations = range(2 ** n)
max_investment = 500
best_investment = ""
best_investment_cost = 0
highest_return = 0

for combination in possible_combinations:
    binary_combi = bin(combination)[2:]
    binary_word = ("0" * (n - len(binary_combi)) + binary_combi)
    combination_cost = 0
    combination_return = 0
    for i in range(n):
        if binary_word[i] == "1":
            combination_cost += stocks[i].cost
            combination_return += stocks[i].cost * stocks[i].ret
    if combination_cost <= max_investment and combination_return > highest_return:
        best_investment = binary_word
        best_investment_cost = combination_cost
        highest_return = combination_return

print("Need to buy : ")
for i in range(len(best_investment)):
    if best_investment[i] == "1":
        print(stocks[i].name)
print()
print(f'Cost : {best_investment_cost}€')
print(f'Profit : {round(highest_return, 2)}€')

print(time.time() - start_time, "seconds")
