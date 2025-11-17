L = [8, 24, 48, 2, 16]

combien = 0
lesquels = []

for nombre in L:
    if nombre % 3 == 0:
        combien += 1
        lesquels.append(nombre)  

print("Nombre de multiples de 3 :", combien)
print("Les multiples de 3 sont :", lesquels)
