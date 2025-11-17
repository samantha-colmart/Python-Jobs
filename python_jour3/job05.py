for num in range(2, 1001):
    premier = True
    
    for i in range(2, num):
        if num % i == 0:
            premier = False
            break
            
    if premier:
        print(num, end = ", ")
