lijst = []

cijfer=int(input("Geef een getal: "))

while cijfer > 0:
    lijst.append(cijfer)
    cijfer = int(input("Geef een getal: "))


print('Er zijn', len(lijst), 'Getallen ingevoerd, de som is:', sum(lijst))