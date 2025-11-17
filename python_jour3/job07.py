alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
index = 0 
ligne = 1 

while index + ligne <= len(alphabet):
    print(alphabet[index:index+ligne])
    index += ligne
    ligne += 1
