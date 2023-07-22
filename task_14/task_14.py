
N = int(input("Введите число N: "))


power = 0
result = 1

print("Целые степени двойки, не превосходящие", N, ":")
while result <= N:
    print(result)
    power += 1
    result = 2 ** power
