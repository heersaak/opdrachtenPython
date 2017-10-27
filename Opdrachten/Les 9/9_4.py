import csv

with open('Artikelen.csv', 'w', newline='') as myCSVfile:
    writer = csv.writer(myCSVfile, delimiter=';')
    writer.writerow(('ArtikelNummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))

    while True:
        ArtikelNummer = input('Voer ArtikelNummer in: ')
        if ArtikelNummer == 'stop':
            break
        ArtikelCode = input('Voer artikelCode in: ')
        Naam = input('Voer het Product in: ')
        Voorraad = input('Hoeveel is er op Voorraad? ')
        Prijs = input('Wat is de Prijs van het product? ')
        writer.writerow((ArtikelNummer, ArtikelCode, Naam, Voorraad, Prijs))
