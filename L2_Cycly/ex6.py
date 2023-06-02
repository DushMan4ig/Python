number = int(input('Введите число: '))
i = 3
fib_one = 0
fib_two = 1
answer = fib_one + fib_two
while answer < number:
    fib_one = fib_two
    fib_two = answer
    answer = fib_one + fib_two
    i = i + 1
print(answer)
if number == answer:
    print(i)
else:
    print(-1)
    

    
