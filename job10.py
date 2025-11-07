montant_initial = 200000
taux_rendement = 8

gain = montant_initial * (taux_rendement / 100)
print("Gain annuel initial :", gain, "€")

montant_initial += 5000
taux_rendement += 2

gain = montant_initial * (taux_rendement / 100)
print("\nAprès ajout de 5000 € et augmentation du taux : 2%")
print("Nouveau montant :", montant_initial, "€")
print("Nouveau taux :", taux_rendement, "%")
print("Nouveau gain annuel :", gain, "€")

montant_initial *= 0.9
taux_rendement -= 1

gain = montant_initial * (taux_rendement / 100)
print("\nAprès retrait de 10 % et baisse du taux : 1%")
print("Montant final :", round(montant_initial, 2), "€")
print("Taux final :", taux_rendement, "%")
print("Gain final :", round(gain, 2), "€")