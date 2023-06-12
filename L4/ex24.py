with open("input.txt", "r") as file:
    N = int(file.readline())  # количество кустов
    berries = list(map(int, file.readline().split()))  # количество ягод на каждом кусте

# Находим куст с максимальным числом ягод
max_berries = max(berries)

# Сумма ягод на всех кустах, за исключением куста с максимальным числом ягод
total_berries = sum(berries) - max_berries

# Выводим результат
with open("output.txt", "w") as file:
    file.write(str(total_berries))