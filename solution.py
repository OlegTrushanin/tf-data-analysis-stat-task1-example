import pandas as pd
import numpy as np


chat_id = 767458283 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    b = np.median(np.abs(x - np.median(x))) / 0.6745
    
    # Находим точечную оценку коэффициента ускорения
    a = 2 * x.mean() / 80 ** 2 / (b * np.sqrt(2))
  
    return a
