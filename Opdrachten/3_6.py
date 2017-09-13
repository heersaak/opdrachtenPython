##Schrijf een for-loop die langs alle letters van een string loopt en de letter uitprint, maar alleen als het
##een klinker is ('aeiou'). Gebruik string s = "Guido van Rossum heeft programmeertaal
##Python bedacht"
text = 'Guido van Rossum heeft programmeertaal Python bedacht'
for x in text:
    if x in 'aeoiu':
        print(x)