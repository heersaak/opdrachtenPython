def namen():

    teller = {}
    while True:
        invoer = input('Volgende naam: ')
        if invoer == '':
            for value in teller:
                if teller[value] == 1:
                    print('Er is {} student met de naam {}'.format(teller[value], value))
                else:
                    print('Er zijn {} studenten met de naam {}'.format(teller[value], value))
            break

        if invoer in teller:
            teller[invoer] += 1
        else:
            teller[invoer] = 1

namen()