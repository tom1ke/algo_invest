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


print(time.time() - start_time, "seconds")