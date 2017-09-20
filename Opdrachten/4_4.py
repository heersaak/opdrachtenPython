## Schrijf (en test) een functie new_password() die 2 parameters heeft: oldpassword en newpassword.
## De return-waarde is True als het nieuwe password voldoet aan de eisen. Het nieuwe password wordt
## alleen geaccepteerd als het verschilt van het oude password èn als het minimaal 6 tekens lang is. Als
## dat niet zo is, is de return-waarde False.


def new_password(x,y):
    if len(x) < 6 or x == y:
        print('false')
    else:
        print('true')

oldpassword = input('Wat is je oude wachtwoord? ')
newpassword = input('Wat is je nieuwe Wachtwoord? ')

print(new_password(newpassword,oldpassword))