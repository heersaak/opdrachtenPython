##Schrijf een nieuw programma waarin de gebruiker een woord moet invoeren. Dit woord moet uit vier
##letters bestaan. Is dat niet zo, dan wordt en foutmelding getoond en moet de gebruiker opnieuw een
##woord invoeren, net zolang totdat er een woord is ingevoerd dat uit vier letters bestaat. Dan eindigt
##het programma. Gebruik in ieder geval een while-loop, gecombineerd met het break-statement!

woord = input("Geef een string van vier letters: ")

while len(woord) > 4 or len(woord) < 4:
    if True:
        print(woord, 'heeft', len(woord), 'letters')
        woord = input("Geef een string van vier letters: ")
    if False:
        break

print('Inlezen van correcte string:', woord, 'is geslaagd')