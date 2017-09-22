## Schrijf functie standaardprijs(afstandKM). Iedere treinrit kost 80 cent per kilometer, maar als de rit
## langer is dan 50 kilometer betaal je een vast bedrag van €15,- plus 60 cent per kilometer. Ga bij invoer
## van negatieve afstanden uit van een afstand van 0 kilometer (prijs is dan dus 0 Euro).

aantalkm = float(input('Hoeveel kilometer is de rit? '))

def standaardprijs(afstandKM):
    if afstandKM in range(0,50):
        print(afstandKM*0.80)

    else:
        print((afstandKM-50)*0.6 + 15)


print(standaardprijs(aantalkm))