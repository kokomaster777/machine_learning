import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Проверяем, существует ли папка models, если нет — создаем её
if not os.path.exists('models'):
    os.makedirs('models')

# Загружаем данные
X_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv")

# Обучаем модель
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Сохраняем модель в файл
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)
