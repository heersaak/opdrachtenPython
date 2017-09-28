##Schrijf een Python programma waarmee je het bestand opent, en splits elke regel op de komma en
##zorg dat de uitvoer (op het scherm) is zoals op de volgende pagina is weergegeven! Vergeet niet het
##bestand te sluiten!

infile = open('kaartnummers.txt', 'r')
text = infile.readlines()

def split():
    for i in text:
        a,b=i.split(",")
        c = b.replace('\n', '')
        print(c, 'Heeft kaartnummer:', a)

infile.close()

print(split())
