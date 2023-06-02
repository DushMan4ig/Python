Numbers_coin = int(input('Введите количество монеток: '))

coins = list(map(int, input().split()))

count_heads = coins.count(1)
count_tails = coins.count(0)

min_flips = min(count_heads, count_tails)

print(min_flips)