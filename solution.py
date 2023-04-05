import pandas as pd
import numpy as np
from scipy.optimize import minimize

chat_id = 767458283 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = x.mean()
    b = (np.abs(x - mu)).mean()
    return 2/b**2
