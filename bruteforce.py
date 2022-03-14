import csv
import time
from dataclasses import dataclass
from pprint import pprint

start_time = time.time()


@dataclass
class Stock:
    name: str
    cost: float
    ret: float


with open("data/dataset_light.csv", "r") as dataset:
    data_reader = csv.reader(dataset)
    next(data_reader, None)
    stocks = []
    for line in data_reader:
        name = line[0]
        cost = float(line[1])
        ret = float(line[2])

        if cost > 0 and ret > 0:
            stock = Stock(name, cost, ret)
            stocks.append(stock)

n = len(stocks)
possible_combinations = range(2 ** n)
binary_list = [bin(i)[2:] for i in possible_combinations]
binary_words = ["0"*(n-len(k)) + k for k in binary_list]

max_investment = 500
valid_investments = []
for combination in binary_words:
    combination_cost = 0
    combination_return = 0
    for i in range(n):
        if combination[i] == "1":
            combination_cost += stocks[i].cost
            combination_return += stocks[i].cost * stocks[i].ret
    if combination_cost <= max_investment:
        valid_investments.append((combination, combination_cost, combination_return))

best_investment = valid_investments[0][0]
best_investment_cost = valid_investments[0][1]
highest_return = valid_investments[0][2]
for combination in valid_investments:
    if combination[2] > highest_return:
        best_investment = combination[0]
        best_investment_cost = combination[1]
        highest_return = combination[2]

stocks_to_buy = [
    stocks[i].name
    for i in range(len(best_investment))
    if best_investment[i] == "1"
]

stocks_to_buy = f'Actions à acheter : {stocks_to_buy}'
best_investment_cost = f'Coût de l\'investissement : {best_investment_cost}€'
highest_return = f'Retour sur investissement : {round(highest_return, 2)}€'

pprint((stocks_to_buy, best_investment_cost, highest_return))

print(time.time() - start_time, "seconds")
