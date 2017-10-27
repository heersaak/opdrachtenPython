stations = ['Schagen', 'Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel','Utrecht Centraal',''''s-Hertogenbosch''','Eindhoven','Weert','Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    while True:
        invoer = input('Vul hier het beginstation in: ')
        if invoer in stations:
            return(invoer)

beginstation = inlezen_beginstation(stations)

def inlezen_eindstation(stations,beginstation):
    while True:
        invoer = input('vul hier het eindstation in: ')
        if invoer in stations:
            if stations.index(invoer) > stations.index(beginstation):
                return(invoer)
            else:
                print('Deze trein komt niet in {}'.format(invoer))
        else:
            print('Deze trein komt niet in {}'.format(invoer))

eindstation = inlezen_eindstation(stations, beginstation)
afstand = stations.index(eindstation) - stations.index(beginstation)
prijs = 5 * afstand
begin = stations.index(beginstation) + 1
eind = stations.index(eindstation) + 1

def omroepen_reis(stations, beginstation, eindstation):
    print('Het beginstation {} is het {}e station in het traject'.format(beginstation,begin))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation,eind))
    print('De afstand bedraagt {} station(s).'.format(afstand))
    print('De prijs van het kaartje is {} euro.\n'.format(prijs))
    print('Jij stapt in de trein in: {}\n'.format(beginstation))

    tussen = stations[stations.index(beginstation) + 1:stations.index(eindstation)]
    print('tussenstations:')
    for x in tussen:
        print('- {}'.format(x))
    print('\nJij stapt uit in: {}'.format(eindstation))


omroepen_reis(stations, beginstation, eindstation)