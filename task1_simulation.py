"""
There are n + 1 people.
At each step, each pearson that has received at least one message at the previous step,
sends two messages to two random distinct people.
(at the beginning, the first person «receives» a message)

What's the median of steps until the last person receives a message (n is considered big enough)?

The claim is that the median is ≈ log_2(n)
This is shown theoretically in the Appendix (see github)

Here (((we))) simulate this process and demonstrate the curve for a big n
"""
import math
import random

import matplotlib.pyplot as plt


def simulate(n, r):
    """ Simulate the process described above for n people and r repetitions """
    wave_size_dynamic = []

    last_wave = {1}  # At the beginning, the first person «receives» a message

    for _ in range(r):
        this_wave = set()

        for person in last_wave:
            # Pick two random _distinct_ people
            person1, person2 = random.sample(range(1, n + 1), 2)

            this_wave.add(person1)
            this_wave.add(person2)

        last_wave = this_wave
        wave_size_dynamic.append(len(last_wave))

    return wave_size_dynamic


def main():
    n = 10000000
    r = int(math.log2(n)) - 2
    print(f'Number of people: {n}, number of repetitions: {r}')

    wave_size_dynamic = simulate(n, r)
    exp_2 = [2 ** i for i in range(1, r + 1)]

    plt.plot(wave_size_dynamic)
    plt.plot(exp_2)
    plt.legend(['Simulation', '2^i'])
    plt.xlabel('i')
    plt.ylabel('Number of people that received a message')
    plt.show()


if __name__ == '__main__':
    main()