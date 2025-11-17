def aliments_saison (type, saison) :
    if type == "fruits" and saison == "hiver" :
        print ("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été" :
        print ("poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver" :
        print ("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été" :
        print("artichaut, aubergine, navet")
    else :
        print ("Aucun aliment correspondant")

aliments_saison ("fruits", "hiver")
aliments_saison ("fruits", "été")
aliments_saison ("légumes", "hiver")
aliments_saison ("légumes", "été")
aliments_saison ("fruits", "printemps") 