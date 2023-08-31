import pandas as pd

# Загрузка данных из sklearn
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Находим минимальное значение population
min_population = df['Population'].min()

# Фильтруем строки с минимальным значением population
min_population_data = df[df['Population'] == min_population]

# Находим максимальное значение households в этой подвыборке
max_households_in_min_population = min_population_data['target'].max()

print("Максимальное количество households в зоне с минимальным значением population:", max_households_in_min_population)
