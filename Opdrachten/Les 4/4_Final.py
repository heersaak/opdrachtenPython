## Schrijf functie standaardprijs(afstandKM). Iedere treinrit kost 80 cent per kilometer, maar als de rit
## langer is dan 50 kilometer betaal je een vast bedrag van €15,- plus 60 cent per kilometer. Ga bij invoer
## van negatieve afstanden uit van een afstand van 0 kilometer (prijs is dan dus 0 Euro).

leeftijd = eval(input('Wat is je leeftijd? \n'))  # functie standaarttarief wordt aangeroepen
tarief = eval(input('Hoeveel KM is de rit? \n'))

def standaardtarief(afstandKM):
    if afstandKM > 50:
        tarief = 15+ 0.6*afstandKM
        return tarief
    elif afstandKM < 0:
        tarief = 0
        return tarief
    else:
        tarief = afstandKM*0.80
        return tarief

def ritprijs(weekend):
    if leeftijd < 12 or leeftijd >=65:
        if weekend == True:
            sTarief = standaardtarief(tarief)*0.65
            return sTarief
        else:
            sTarief = standaardtarief(tarief)*0.70
            return sTarief
    else:
        if weekend == True:
            sTarief = standaardtarief(tarief)*0.6
            return sTarief
        else:
            return standaardtarief(tarief)

print(ritprijs(True),'euro')