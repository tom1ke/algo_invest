import time
import csv
from dataclasses import dataclass

start_time = time.time()


@dataclass
class Stock:
    """
    Dataclass permettant d'instancier des objets "Actions"
    Attributs :
    - Nom
    - Coût
    - Rendement
    """
    name: str
    cost: float
    ret: float


# Variables contenant les chemins d'accès aux différents datasets
dataset0 = "data/dataset_light.csv"
dataset1 = "data/dataset1_Python+P7.csv"
dataset2 = "data/dataset2_Python+P7.csv"

# Lecteur CSV prenant l'une des variables précédentes comme source
with open(dataset0, "r") as dataset:
    data_reader = csv.reader(dataset)
    next(data_reader, None)
    stocks = []
    # Traitement des données du CSV
    for line in data_reader:
        name = line[0]
        cost = float(line[1])
        ret = float(line[2]) / 100

        # Filtrage des données du CSV, création d'objets Stock et ajout à la liste des actions
        if cost > 0 and ret > 0:
            stock = Stock(name, cost, ret)
            stocks.append(stock)

# Nombre d'actions contenue dans la liste
n = len(stocks)

# Calcul du nombre de possibilités d'investissement
possible_combinations = range(2 ** n)

max_investment = 500

# Valeurs par défaut des variables utiles à l'algorithme
best_investment = ""
best_investment_cost = 0
highest_return = 0

for combination in possible_combinations:
    # Conversion de l'index en binaire sans les deux premiers caractères
    binary_combi = bin(combination)[2:]
    # Ajout de 0 pour obtenir un mot binaire de longueur n
    binary_word = ("0" * (n - len(binary_combi)) + binary_combi)
    combination_cost = 0
    combination_return = 0
    for i in range(n):
        # À chaque 1 trouvé dans le mot binaire représentant la combinaison, ajout du prix et du profit de l'action
        if binary_word[i] == "1":
            combination_cost += stocks[i].cost
            combination_return += stocks[i].cost * stocks[i].ret
    if combination_cost <= max_investment and combination_return > highest_return:
        # Garde les valeurs en mémoire si la combinaison est valide
        best_investment = binary_word
        best_investment_cost = combination_cost
        highest_return = combination_return

print("Need to buy : ")
# Identification des actions contenues dans la  meilleure combinaison
for i in range(len(best_investment)):
    if best_investment[i] == "1":
        print(stocks[i].name)
print()
print(f'Cost : {best_investment_cost}€')
print(f'Profit : {round(highest_return, 2)}€')

print(time.time() - start_time, "seconds")
