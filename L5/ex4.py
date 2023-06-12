def sequence(size):
    if size == 0:
        return ''
    variable = input('Введите число: ')
    return sequence(size - 1) + variable
print(sequence(4))