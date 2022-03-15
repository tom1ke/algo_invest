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
max_investment = 500
stocks_to_buy = []
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
