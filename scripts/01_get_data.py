import os
import pandas as pd

# Проверяем, существует ли папка data, если нет — создаем её
if not os.path.exists('data'):
    os.makedirs('data')

# Загружаем данные и сохраняем в файл
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
df.to_csv("data/raw.csv", index=False)
