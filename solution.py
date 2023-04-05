import pandas as pd
import numpy as np


chat_id = 767458283 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    def log_likelihood(x, t):
         b = np.median(np.abs(x - np.median(x))) / 0.6745
         a = 2 * x.mean() / t ** 2 / (b * np.sqrt(2))
         return np.sum(np.log(np.exp(-np.abs(x - a * t) / b) / (2 * b)))

    t = 80
    res = minimize_scalar(lambda t: -log_likelihood(x, t), bounds=(0.01, 1000), method='bounded')
    return 2 * x.mean() / res.x ** 2 / (np.median(np.abs(x - np.median(x))) / 0.6745 * np.sqrt(2))
