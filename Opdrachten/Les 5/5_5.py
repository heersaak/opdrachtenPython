##Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin in te voeren. De functie
##berekent vervolgens de gemiddelde lengte van de woorden in de zin en print dit uit.

zin = input('Vul hier een random zin in: ')

def gem(x):
    y = list(map(len, x.split()))
    return sum(y) / len(y)

print('De gemiddelde lengte van de woorden zijn:',gem(zin))