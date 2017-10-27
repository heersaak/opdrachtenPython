def ticker():
    dict = {}
    file = open('ticker.txt')
    content = file.readlines()
    file.close()
    for i in content:
        i = i.strip().split(':')

        bedrijf = i[1]
        symbol = i[0]
        dict[symbol] = bedrijf


    while True:
        invoer = input('Vul bedrijfsnaam in: ')
        invoer.upper()
        if invoer in dict:
            regel = 'Ticker symbool: '
            print(regel + dict[invoer])


ticker()