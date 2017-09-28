##Schrijf een functie convert() waar je een temperatuur in graden Celsius (als parameter van deze
##functie) kunt omzetten naar graden Fahrenheit. Je kunt de temperatuur in Fahrenheit berekenen met
##de formule T(°F) = T(°C) × 1.8 + 32. Dus 25 °C = 25 * 1.8 + 32 = 77 °F.

##Schrijf nu ook een tweede functie table() waarin je met een for-loop van -30 °C t/m 40 °C in stappen
##van 10 graden de temperatuur in Fahrenheit print. Zorg middels een geformatteerde output voor
##dezelfde precisie en uitlijning als het voorbeeld hieronder:


def convert(Celcius):
    fah = Celcius * 1.8 +32
    return fah

def table():
    print(' {:7} {}'.format("F", "X"))
    for x in range(-30, 50, 10):
        print( '{:5} {:5}'.format(convert(x), x))

print(table())


