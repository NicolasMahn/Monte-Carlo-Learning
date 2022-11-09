import matplotlib.pyplot as plt
import random

import numpy as np


def monte_carlo_simple():

    rounds = list()
    for episode in range(0, 1000000):  # 1 million episodes are played
        p = 1
        round_ = 0
        euro = 4
        while euro >= 2:   # The number of states differs in every episode
            euro -= 2
            round_ += 1
            if random.random() < p:
                p -= 0.1 * random.random()
                euro += 3
        rounds.append(round_)
    return sum(rounds)/len(rounds)  # >> 20.511079


def monte_carlo_learning():
    return_ = dict()  # all returns collected in an episode
    n = np.full([30], 0)  # number of times a state has been tread upon
    v = np.full([30], 0, dtype=float)  # V starting with the random number 0
    for episode in range(0, 1000000):  # 1 million episodes are played
        p = 1
        round_ = 0  # state
        euro = 4  # reward
        while euro >= 2 and round_ < 29:
            euro -= 2
            round_ += 1
            if random.random() < p:
                p -= 0.1 * random.random()
                euro += 3
            return_[round_] = euro
            n[round_] += 1

        for round_ in return_:
            v[round_] = v[round_] + (1 / n[round_]) * (return_[round_] - v[round_])
    return v  # argmax(v) >> 10


def plot_v(v):
    plt.title("Value of each State")
    plt.xlabel("round | state")
    plt.ylabel("average return")
    plt.xlim([0, 30])
    plt.ylim([0, 9])
    plt.plot(v, color="#008854")
    plt.show()


def main():

    v = monte_carlo_learning()

    print(np.argmax(v))
    print(v)

    plot_v(v)







if __name__ == '__main__':
    main()
