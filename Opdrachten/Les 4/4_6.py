## Schrijf (en test) functie wijzig() met één parameter: letterlijst. Zorg dat de functie de lijst leegt en de
## letters [ ‘d’, ‘e’, ‘f’ ] toevoegt. Er is geen return-waarde! Test je programma als volgt:
## lijst = ['a', 'b', 'c']
## print(lijst)
## wijzig(lijst)
## print(lijst)

lijst = ['a','b','c']

def wijzig (letterlijst):
    letterlijst.pop(0)
    letterlijst.insert(0, 'd')
    letterlijst.pop(1)
    letterlijst.insert(1, 'e')
    letterlijst.pop(2)
    letterlijst.insert(2, 'f')


print(lijst)
wijzig(lijst)
print(lijst)