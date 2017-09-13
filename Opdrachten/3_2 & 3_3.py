##Je mag stemmen als je 18 of ouder bent èn in het bezit bent van een Nederlands paspoort. Schrijf een
##programma dat de leeftijd van de gebruiker vraagt en of diegene een Nederlands paspoort heeft
##(ja/nee). Als aan beide voorwaarden is voldaan, print dan dat de gebruiker mag stemmen! Doe dit
##weer in een nieuw bestand, bijvoorbeeld pe2_3.py. In de conditie van een if-statement kun je
##meerdere voorwaarden tegelijk controleren met bijvoorbeeld or of and (zie Perkovic blz 18 en 19).
##Voor deze opgave mag je daarom maximaal 1 keer een if-statement gebruiken.

paspoort= input('Heb jij een nederlands paspoort? ')
leeftijd=int(input('Hoe oud ben je? '))
if paspoort=='ja' and leeftijd >= 18:
    print('Je mag stemmen')
else: print('Je mag niet stemmen')
