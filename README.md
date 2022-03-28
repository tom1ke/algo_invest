# Algo Invest & Trade

Version : Python 3.10.1

## Paramétrage
- Cloner le repository
- Créer un environnement virtuel à la racine du projet avec la commande

```
 python3 -m venv env
```

- Activer l'environnement virtuel avec la commande

```
source env/bin/activate
```

## Exécution des scripts
- Ouvrir un terminal
- Se positionner à la racine du projet
- Lancer le script voulu avec la commande

```
python3 bruteforce.py
```
ou
```
python3 optimized.py
```

## Choix de l'ensemble de données
Il est possible de modifier au sein des scripts l'ensemble de données à traiter.
Les 3 ensembles de données concernés sont attribués à des variables :
```
dataset0 = "data/dataset_light.csv"
dataset1 = "data/dataset1_Python+P7.csv"
dataset2 = "data/dataset2_Python+P7.csv"
```

Pour faire la modification, il faudra ouvrir le script correspondant avec un éditeur de texte ou un IDE  et modifier
cette ligne en y mettant la variable correspondant au dataset voulu:
```
with open(dataset0, "r") as dataset:
```