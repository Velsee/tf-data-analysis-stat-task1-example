import pandas as pd
import numpy as np


chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 2 # количество дней для оценки
    n = len(x) # количество компаний-партнеров
    x = x.sum()/(t*n)
    return x.mean() # Ваш ответ
