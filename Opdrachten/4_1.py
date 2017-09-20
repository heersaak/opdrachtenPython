## Maak een nieuwe Python file aan voor deze opdracht (vanaf nu is dat standaard en zal dat niet steeds
## meer bij de opdracht staan). Schrijf (en test) de functie som() die 3 parameters heeft: getal1, getal2
## en getal3. De return-waarde van de functie moet de som (optelling) van deze parameters zijn!

getal1 = 1
getal2 = 2
getal3 = 3

def som(*x):
    return sum(x)

print(som(getal1,getal2,getal3))