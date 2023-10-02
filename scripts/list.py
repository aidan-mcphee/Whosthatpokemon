import csv

pokedict = {}

with open('pokemon.csv', 'r') as pokemon:
    reader = csv.reader(pokemon)
    for row in reader:
        pokedict[row[0]] = row[1]