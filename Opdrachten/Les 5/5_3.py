##Schrijf een programma dat het bestand kaartnummers.txt opnieuw opent en het aantal regels en het
##grootste kaartnummer in het bestand bepaalt. Print deze gegevens vervolgens uit:

infile = open('kaartnummers.txt', 'r')
text = infile.readlines()

for word in text:
    dit = word.split()

infile.close()

