##Schrijf een nieuw programma waarin een list met minimaal 10 strings wordt ingelezen. Het programma
##plaatst alle vier-letter strings uit de ingelezen list in een nieuwe list en drukt deze af. Inlezen van een
##lijst kan met eval(input("Geef lijst met minimaal 10 strings: ")).

lijst = eval(input("Geef lijst met minimaal 10 strings: "))

vierlijst = []

for i in lijst:
    if len(i) <= 4:
        vierlijst.append(i)
print("De nieuw-gemaakte lijst met alle vier-letter strings is:")
print(vierlijst)