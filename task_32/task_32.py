def find_indices_in_range(lst, min_val, max_val):
    indices = []
    for i, num in enumerate(lst):
        if min_val <= num <= max_val:
            indices.append(i)
    return indices


my_list = [10, 25, 7, 15, 30, 5, 18, 22] #это пример
min_value = 10
max_value = 20

result_indices = find_indices_in_range(my_list, min_value, max_value)

print(f"Индексы элементов, значение которых находится между {min_value} и {max_value}: {result_indices}")
