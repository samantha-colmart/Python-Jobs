# pas compris l'exercice

L = [7, 11, 42, 39, 2]

i = 0
while i < 5:
    j = i + 1
    while j < 5:
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
        j += 1
    i += 1

print("Liste triée :", L)
