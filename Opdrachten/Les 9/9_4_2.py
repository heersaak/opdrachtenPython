import csv

with open ('Artikelen.csv', 'r') as csvwerken:
    reader = csv.DictReader(csvwerken, delimiter=';')

    prijzen = []

    for row in reader:
        artPrijs = row['Prijs']
        prijzen.append(artPrijs)
print(min(prijzen))
print(max(prijzen))
print(prijzen)
prijzen.sort()
print(prijzen)
