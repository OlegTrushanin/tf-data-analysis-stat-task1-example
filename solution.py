import pandas as pd
import numpy as np


chat_id = 767458283 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    b = np.median(np.abs(x - np.median(x))) / 0.6745
    
    # Находим точечную оценку коэффициента ускорения
    a = 2 * x.mean() / 80 ** 2 / (b * np.sqrt(2))
    sample_sizes = [10, 100, 1000]
    thresholds = [2.14E-8, 6.26E-9, 1.94E-9]
    for i in range(len(sample_sizes)):
        sample_size = sample_sizes[i]
        threshold = thresholds[i]
        mse = np.mean((x[:sample_size] - a * np.arange(80) ** 2 / 2) ** 2)
    return a
