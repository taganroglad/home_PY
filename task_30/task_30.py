a1 = float(input("Введите первый элемент прогрессии (a1): "))
d = float(input("Введите разность прогрессии (d): "))
n = int(input("Введите количество элементов: "))

progression = []
for i in range(n):
    an = a1 + i * d
    progression.append(an)
print("Элементы арифметической прогрессии:")
for num in progression:
    print(num)
