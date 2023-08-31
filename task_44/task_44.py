import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = data.pivot_table(index=data.index, columns='whoAmI', aggfunc=len, fill_value=0)

print(one_hot_data)
