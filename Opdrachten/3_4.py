##Schrijf een for-loop die over een lijst met strings itereert, en van elk woord de eerste twee karakters
##print. De lijst [ ‘maandag’, ‘dinsdag’, ‘woensdag’ ] zou dus moeten resulteren in:
##ma
##di
##wo



list = ['maandag', 'dinsdag', 'woensdag']
for x in list:
    print(x[0]+x[1])