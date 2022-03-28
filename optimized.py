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
    cost: int
    profit: float


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
        # Le prix est multiplié par 100 pour obtenir un entier
        cost = int(float(line[1]) * 100)
        profit = float(line[2]) / 100

        # Filtrage des données du CSV, création d'objets Stock et ajout à la liste des actions
        if cost > 0 and profit > 0:
            stock = Stock(name, cost, profit)
            stocks.append(stock)


# Nombre d'actions contenue dans la liste
n = len(stocks)

max_investment = 50000

# Listes des prix et des profits de toutes les actions
costs = [i.cost for i in stocks]
profits = [i.cost * i.profit for i in stocks]


def solve_dynamic(profits, weights, capacity):
    """
    Fonction permettant de déterminer le meilleur profit
    :param profits: liste des profits des actions
    :param weights: liste des prix des actions
    :param capacity: valeur de l'investissement maximal autorisé
    :return: la valeur contenue dans la dernière case du tableau en bas à droite = meilleur profit
    """

    # Conditions de base
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    # Création du tableau vide
    table = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    for i in range(n):
        # Initialisation de la première colonne
        table[i][0] = 0

    for c in range(capacity + 1):
        # Initialisation de la première ligne
        if weights[0] <= c:
            table[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + table[i - 1][c - weights[i]]
            profit2 = table[i - 1][c]
            table[i][c] = max(profit1, profit2)

    # Appel de la fonction pour afficher les actions sélectionnées et le coût global de l'investissement
    print_selected_stocks(table, profits, weights, capacity)
    return table[n - 1][capacity]


def print_selected_stocks(table, profits, weights, capacity):
    """
    Fonction permettant de déterminer les actions choisies et leur prix
    :param table: tableau contenant les valeurs de profits calculées
    :param profits: liste des profits des actions
    :param weights: liste des prix des actions
    :param capacity: valeur de l'investissement maximal autorisé
    :return: les actions sélectionnées et la valeur globale de l'investissement
    """
    print("Need to buy: ", end='\n')
    investment_cost = 0
    # Valeur du meilleur profit
    total_profit = table[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        try:
            if total_profit != table[i - 1][capacity] and weights[i] <= capacity:
                # Si le profit est différent de celui de la case du dessus, l'action a été sélectionnée
                print(f'{str(stocks[i].name)} ', end='\n')
                # Son prix est ajouté au coût global
                investment_cost += weights[i]
                # On soustrait son prix à la capacité et son profit au profit global pour trouver la prochaine valeur
                capacity -= weights[i]
                total_profit -= profits[i]
        except IndexError:
            break

    if total_profit != 0 and weights[0] <= capacity:
        print(f'{str(stocks[0].name)} ', end='')
        investment_cost += weights[0]
    print()
    print(f'Cost : {investment_cost / 100}€')


# Valeur retournée par l'algorithme divisé par 100 pour correspondre aux valeurs initiales
highest_profit = solve_dynamic(profits, costs, max_investment) / 100
print(f'Profit : {round(highest_profit, 2)}€')

print(time.time() - start_time, "seconds")
