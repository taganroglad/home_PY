n = int(input("Введите количество монеток (n): "))
coins = input("Введите последовательность монеток (например, 'HHHTTT'): ")

heads = coins.count('H')
tails = n - heads

min_flips = min(heads, tails)


print(f"Минимальное количество монет, которые нужно перевернуть: {min_flips}")
