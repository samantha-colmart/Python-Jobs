L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme_paires = 0
nombres_pairs = []

for nombre in L:
    if nombre % 2 == 0:
        somme_paires += nombre
        nombres_pairs.append(nombre)

nombres_pairs.sort()

print("La somme des nombres pairs de la liste est :", somme_paires)
print("Les nombres pairs de la liste sont :", nombres_pairs)