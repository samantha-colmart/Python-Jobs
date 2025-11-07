nom_produit = "Photobook"
prix_unitaire = 26.5
quantite_stock = 6

print("Informations sur le produit :")
print(f"Nom de produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} €")
print(f"Quantité en stock : {quantite_stock}")

quantite_achat = int(input("Combien de produits voulez-vous acheter ? "))
quantite_stock -= quantite_achat 

prix_unitaire *= 1.10 

print("\nInformations mises à jour :")
print(f"Nom : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire:.2f} €")
print(f"Quantité en stock : {quantite_stock}")