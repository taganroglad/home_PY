
berries = [int(x) for x in input("Введите количество ягод на каждом кусте через пробел: ").split()]

n = len(berries)
max_collected = 0

# Обрабатываем каждый куст и его двух соседей
for i in range(n):
    collected = berries[i] + berries[(i+1) % n] + berries[(i+2) % n]
    max_collected = max(max_collected, collected)

# Выводим результат
print("Максимальное количество ягод, которое может собрать собирающий модуль за один заход:", max_collected)
