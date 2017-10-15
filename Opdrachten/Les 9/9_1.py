try:
    invoer = int(input('Hoeveel personen gaan mee op reis?: '))
    if invoer < 0:
        print('Negatieve getallen zijn niet toegestaan.')
    else:
        print('Je betaald:',4356/invoer, 'per persoon')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het getal!')
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except:
    print('Overige error')
