
invoer = input('vul hier je code in: ')

def geheimecode(invoerstring):

    tekst = ''
    totaal = []
    for char in invoerstring:
        ascii = ord(char)
        drie = ascii + 3
        totaal.append(drie)


    for i in totaal:
        plain = chr(i)
        tekst += plain

    print('De uitkomst is: {} '.format(tekst))




geheimecode(invoer)