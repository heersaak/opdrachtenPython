##De Hogeschool Utrecht wil studenten financieel ondersteunen bij hun studie, afhankelijk van de cijfers
##die een student haalt. Voor elk cijferpunt krijg je € 30,-. Voor een 1,0 krijgt je dus 30 euro, voor een 2,5
##krijgt je 75 euro en voor een 10,0 beloont de HU een student met € 300,-.
##Maak variabelen cijferICOR, cijferPROG en cijferCSN. Geef ze alle drie de waarde die jij verwacht dat
##je voor de betreffende vakken in blok 1 zult gaan halen. Maak nu vervolgens ook de volgende
##variabelen aan, en bereken de bijbehorende waarden m.b.v. een Python expressie:
##gemiddelde het gemiddelde van de variabelen cijferICOR, cijferPROG en cijferCSN.
##beloning de totale beloning voor deze drie cursussen.
##overzicht een string met een tekstuele omschrijving het gemiddelde en de beloning:


cijferICOR = int(7)
cijferCSN = int(8)
cijferPROG = int(7)
beloning = int(30)

print('gemiddeld cijfer:', ((cijferICOR + cijferCSN + cijferPROG)/3))
print('Totale beloning:', ((beloning*cijferPROG)+(beloning*cijferCSN)+(beloning*cijferICOR)))
print('beloning Programeren:',beloning*cijferPROG)
print('beloning CSN:',beloning*cijferCSN)
print('beloning ICOR:',beloning*cijferICOR)
