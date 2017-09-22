##Schrijf een programma dat de gebruiker vraagt om de score van een multiplechoice toets. Het
##programma bepaalt of het resultaat voldoende is. Bij meer dan 15 punten is de deelnemer geslaagd!

score = float(input('Wat is de score van je toets?:'))
if score>15:
    print('Je hebt een voldoende!')
else: print('Je hebt een onvoldoende, volgende keer beter')