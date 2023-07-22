# Ввод данных от пользователя
summa = int(input("Введите сумму чисел (Summa): "))
proizv = int(input("Введите произведение чисел (Proiz): "))

# Поиск чисел X и Y
for Y in range(1, summa + 1):
    X = summa - Y
    if X * Y == proizv:
        print(f"Числа X и Y: {X}, {Y}")
        break
else:
    print("Числа X и Y не могут быть найдены для заданных суммы и произведения.")
