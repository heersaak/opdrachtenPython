##Gegeven is variabele invoer = "5-9-7-1-7-8-3-2-4-8-7-9". Schrijf een nieuw programma
##waarin je deze variabele splitst in een lijst van getallen en print de gesorteerde lijst. Bepaal en print na
##het opsplitsen de grootste waarde, kleinste waarde, aantal getallen, de som en het gemiddelde!

invoer = [1, 2, 3, 4, 5, 7, 7, 7, 8, 8, 9, 9]
gesorteerd = sorted(invoer)

print('Gesorteerde list van ints:', gesorteerd)
print('Grootste getal:', max(invoer), 'en het Kleinste getal:', min(invoer))
print('aantal getallen:', len(invoer), 'en Som van de getallen:', sum(invoer))
print('Gemiddelde:', sum(invoer)/len(invoer))