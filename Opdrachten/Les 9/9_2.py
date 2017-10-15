import csv
import datetime

bestand = 'inloggers.csv'

with open('inloggers.csv', 'a', newline='') as inloggers:
    writer = csv.writer(inloggers, delimiter=';')
    writer.writerow(('tijd', 'naam', 'voorl', 'gbdatum', 'email'))

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        vandaag = datetime.datetime.today()
        time = vandaag.strftime("%a %d %b %Y %H:%M")

        writer.writerow((time, naam, voorl, gbdatum, email))

