import math
import statistics

import numpy as np

DELTA = 0.05
EPSILON = 0.01

def estimate_n_chebyshev(lam):
    return lam / (DELTA * EPSILON**2)

def estimate_clt(lam):
    return (lam * 1.96**2) / EPSILON**2

def validate_estimator(lam, times: int, estimator_name: str):
    acceptable = 0
    trials = 20
    for _ in range(trials):
        values = [float(x) for x in np.random.poisson(lam, times)]
        avr = statistics.mean(values)
        # = list(filter(lambda v: abs(v - lam) <= EPSILON, values))
        # print(f"{len(acceptable)}/{times}")
        if abs(avr - lam) <= EPSILON:
            acceptable += 1
    print(f"{estimator_name}: {times} times taken, acceptable share: {acceptable / trials}")



for lam in [0.5, 1, 5, 9]:
    print(f"Results for lambda = {lam}:")
    validate_estimator(lam, math.ceil(estimate_n_chebyshev(lam)), "Чебышев")
    # validate_estimator(lam, math.ceil(estimate_clt(lam)), "ЦПТ")


"""
Results for lambda = 0.5:
ЦПТ: 19208 times taken, acceptable share: 0.96
Results for lambda = 1:
ЦПТ: 38416 times taken, acceptable share: 0.95
Results for lambda = 5:
ЦПТ: 192080 times taken, acceptable share: 0.97
Results for lambda = 9:
ЦПТ: 345744 times taken, acceptable share: 0.95
"""
