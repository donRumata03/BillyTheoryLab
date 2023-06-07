import math
import statistics
import time

import numpy as np
import scipy
from scipy.stats.sampling import TransformedDensityRejection


def pdf(x):
    return 5 * x ** 4 / (2 * math.pi) ** 0.5 * math.exp(-(5 - x ** 2) ** 2 / 2)


def dpdf(x):
    return -(5 * math.exp(-1 / 2 * (x ** 5 - 5) ** 2) * x ** 3 * (5 * x ** 10 - 25 * x ** 5 - 4)) / math.sqrt(2 * math.pi)

def cdf_inversed(alpha):
    return (scipy.special.erfinv(2 * (alpha - 0.5)) * math.sqrt(2) + 5) ** (1 / 5)


class MyDist(scipy.stats.rv_continuous):
    def __init__(self):
        super().__init__(momtype=0, a=1, b=2)

    def _pdf(self, x, *args):
        return pdf(x)

    def dpdf(self, x, *args):
        return dpdf(x)

    def support(self):
        return (1.5, 1.6)

def generate_derived(samples):
    dist = MyDist()
    urng = np.random.default_rng()
    return dist.rvs(size=samples)

def generate_inverse(samples):
    dist = MyDist()
    urng = np.random.default_rng()
    return [cdf_inversed(urng.random()) for _ in range(samples)]


def generate_rejection(samples):
    dist = MyDist()

    urng = np.random.default_rng()
    rng = TransformedDensityRejection(dist, domain=dist.support(), random_state=urng)
    print(rng.rvs(1000))

def measure_time(f):
    start = time.time()
    f()
    return time.time() - start

def measure(samples, generator):
    measurements = 1000_000
    times = int(measurements / samples)
    average = measure_time(lambda: [generator(samples) for _ in range(times)]) / times
    print(f"Average of {average} seconds at {samples} samples")


if __name__ == '__main__':
    # print(generate_derived(10))
    # print(generate_inverse(10))
    # print(generate_rejection(10)) # Use scipy's rejection sampling method (as suggested in the statement)

    for s in [100, 1000, 10000, 100000]:
        print("Inverse:")
        measure(samples=s, generator=generate_inverse)

        print("Derived:")
        measure(samples=s, generator=generate_inverse)

        print("Rejecting:")
        measure(samples=s, generator=generate_rejection)
