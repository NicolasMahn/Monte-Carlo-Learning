import matplotlib.pyplot as plt
import numpy.random
import numpy as np

random = numpy.random.random


def very_simple_monte_carlo():

    rounds = list()
    for episode in range(0, 1000000):  # 1 million episodes are played
        p = 1
        round_ = 0
        euro = 4
        while euro >= 2:   # The number of states differs in every episode
            round_ += 1
            if random() < p:
                euro -= 2
                p -= 0.1 * random()
                euro += 3
        rounds.append(round_)
    return sum(rounds)/len(rounds)  # >> 20.511079


def simple_monte_carlo_learning():
    avg_fr = np.full([30], 0, dtype=float)  # avg_fr starting with 0s
    n = np.full([30], 0)  # number of times a state has been tread upon
    for episode in range(1, 10001):  # 10 000 episodes are played

        fr = dict()
        p = 1
        state = 0  # current round
        euro = 4  # reward
        # random policy
        # can't play when gambler doesn't have enough money
        while state < 30:

            euro -= 2
            if random() < p:
                p -= 0.1 * random()
                euro += 3
            fr[state] = euro
            n[state] += 1
            state += 1

        for state in fr:
            avg_fr[state] = avg_fr[state] + \
                            (1 / n[state]) * (fr[state] - avg_fr[state])
    return avg_fr  # argmax(avg_euro) >> 7


def simple_monte_carlo_learning_plot():
    avg_fr_list = list()

    avg_fr = np.full([30], 0, dtype=float)  # avg_fr starting with 0s
    n = np.full([30], 0)  # number of times a round_ has been tread upon
    for episode in range(1, 10001):  # 10 000 episodes are played

        fr = dict()

        p = 1
        round_ = 0  # current round
        euro = 4  # reward
        # random policy
        # can't play when gambler doesn't have enough money
        while round_ < 30:

            euro -= 2
            if random() < p:
                p -= 0.1 * random()
                euro += 3
            fr[round_] = euro
            n[round_] += 1
            round_ += 1

        for round_ in fr:
            avg_fr[round_] = avg_fr[round_] + (1 / n[round_]) * \
                                           (fr[round_] - avg_fr[round_])

        if episode in [1, 10, 100, 1000, 10000]:
            avg_fr_list.append(avg_fr.copy())
    return avg_fr_list  # argmax(avg_fr) >> 7


def plot_avg_euro(v):
    plt.title("Average Euro per Round")
    plt.xlabel("round")
    plt.ylabel("expected average return on investment (€)")
    plt.xlim([0, 30])
    plt.ylim([0, 9])
    plt.plot(v, color="#008855", linewidth=3)
    plt.show()


def plot_avg_euro_list(v_list, v_list_episode_count, legend=True):
    plt.title("Average Euro per Round")
    plt.xlabel("at round")
    plt.ylabel("expected average return on investment (€)")

    colors = ["#880033", "#550088", "#885500", "#007788",  "#008855", "#003388",
              "#338800", "#880077", "#881100", "#778800"]

    for j in range(len(v_list)):
        episode = v_list_episode_count[j]
        if j == len(v_list_episode_count):
            color = "#008854"
        else:
            color = colors[j]
        plt.plot(v_list[j], color=color, label=f"episode {episode}", linewidth=3)
    if legend:
        plt.legend()
    plt.show()


def main():

    print("")

    avg_fr_list = simple_monte_carlo_learning_plot()

    print(np.argmax(avg_fr_list[-1]))
    print(avg_fr_list[-1])

    plot_avg_euro_list(avg_fr_list, [1, 10, 100, 1000, 10000], legend=True)







if __name__ == '__main__':
    main()
