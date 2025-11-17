# pas compris l'exercice

liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
nouvelle_liste = []

for x in liste:
    deja = False
    for y in nouvelle_liste:
        if x == y:
            deja = True
            break
    if not deja:
        nouvelle_liste += [x]

print("Liste sans doublons :", nouvelle_liste)