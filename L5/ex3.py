def prime_numb(num):
    kol = 0
    for i in range(1, num+1):
        if num % i == 0:
             kol += 1
    if kol == 2:
             return(f"Число {num} простое")
    else:
             return(f"Число {num} составное")
print(prime_numb(51))

    
