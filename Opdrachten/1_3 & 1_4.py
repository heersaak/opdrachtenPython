##1. Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b.
a = 6
b = 7
##2. Ken aan variabele c als waarde het gemiddelde van a en b toe.
c = (a+b)/2
##3. Ken aan variabele inventaris de een lijst van strings toe: ‘papier’, ‘nietjes’, en ‘pennen’.
inventaris = ['papier', 'nietjes', 'pennen']
##4. Ken aan variabelen voornaam, tussenvoegsel en achternaam je eigen naamgegevens toe.
voornaam = 'Rik'
tussenvoegsel = 'den'
achternaam = 'Hartog'

##5. Ken aan variabele mijnnaam de variabelen van opdracht 4 (met spaties er tussen) toe.
mijnnaam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam
print(mijnnaam)

## 1_4

##1. 6.75 groter is dan a en kleiner b.
print(6.75 > a)
print(6.75 < b)
##2. de lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam.
print(str(inventaris) > (mijnnaam*5))

##3. de lijst inventaris leeg is, of juist meer dan 10 items bevat.
if inventaris == 0:
    print ('leeg')
if str(inventaris) > str(10):
   print('Meer dan 10 tekens')
