import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

filtered_data = df[(df['Population'] >= 0) & (df['Population'] <= 500)]
average_house_value = filtered_data['target'].mean()
print("Средняя стоимость дома с количеством людей от 0 до 500:", average_house_value)
