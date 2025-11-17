def pair_ou_impair (nombre) :
    if nombre < 0 :
        print ("Erreur : le nombre doit être positif")
        return
    
    if nombre % 2 == 0 :
        print (f"{nombre} est pair")
    else : 
        print (f"{nombre} est impair")


pair_ou_impair(4)
pair_ou_impair(7)
pair_ou_impair(-3)
pair_ou_impair(0)
pair_ou_impair(12)
pair_ou_impair (15)