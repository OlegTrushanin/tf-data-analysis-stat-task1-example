import pandas as pd
import numpy as np
from scipy.optimize import minimize

chat_id = 767458283 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    time = 80.0  # время в секундах
    
    # Средний пройденный путь
    mean_distance = np.mean(x)
    
    
    mean_speed = mean_distance / time  # средняя скорость
    acceleration = mean_speed**2 / (2 * mean_distance)  # оценка ускорения
    
    return acceleration
