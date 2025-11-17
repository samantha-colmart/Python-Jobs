def calcule (num1, operator, num2) :
    if operator == "+" :
        return num1 + num2
    elif operator == "-" :
        return num1 - num2
    elif operator == "*" :
        return num1 * num2
    elif operator == "/" :
        return num1 / num2
    elif operator == "%" :
        return num1 % num2
    else :
        return "Erreur : opération inconnu"

print (calcule (20, "+", 5))
print (calcule (20, "-", 5))
print (calcule (20, "*", 5))
print (calcule (9, "/", 3))
print (calcule (10, "%", 3))
print (calcule (20, "x", 5))