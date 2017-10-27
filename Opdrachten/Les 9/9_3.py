import csv

nummers = []
namen = []
tijden = []

with open ('CSVlezen.csv', 'r') as myCSVfile:
    reader = csv.reader(myCSVfile, delimiter=';')

for row in reader:
    naam = row[0]
    tijd = row[1]
    nummer = row[2]

namen.append(naam)
tijden.append(tijd)
nummers.append(nummer)

hoogstenummer = max(nummers)
nummers.index(hoogstenummer)
score = nummers.index(hoogstenummer)
bestepersoon = namen[score]
wanneer = tijden[score]

print('De hoogste score is', hoogstenummer, 'is behaald door', bestepersoon,'op', wanneer)