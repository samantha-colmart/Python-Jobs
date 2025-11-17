a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if a == b == c :
    print ("C'est un triangle équilatérale")

elif a == b or a == c or b == c :
    print ("C'est un triangle isocèle")
           
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
    print ("C'est un triangle rectangle")

else :
    print ("c'est un triangle quelconque")