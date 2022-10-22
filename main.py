import matplotlib.pyplot as plt
import random

import numpy as np


def monteCarloSimple():

    rounds = list()
    for episode in range(0, 1000000): # 1 million episodes are played
        p = 1
        round = 0
        euro = 4
        while euro >= 2: #The number of states differs in every episode
            euro -= 2
            round += 1
            if random.random() < p:
                p -= 0.1 * random.random()
                euro += 3
        rounds.append(round)
    return sum(rounds)/len(rounds)  # 21.501723


def monteCarloLearning():
    curve = list()
    rewards = list() # all known returns (G)
    stopWhen = 0 # V(s) starting with the random number 0
    for episode in range(0, 2000): # 2 thousand episodes are played
        p = 1
        round = 0
        euro = 4
        while euro >= 2 and stopWhen > round: # The number of states differs in every episode
            euro -= 2
            round += 1
            if random.random() < p:
                p -= 0.1 * random.random()
                euro += 3
        rewards.append(euro)
        stopWhen = stopWhen + (1/len(rewards))*(euro-stopWhen) # Value function
        curve.append(stopWhen)
    return curve # stopWhen is the result, curve is for the figure


def avgReturnsAt(stopWhen):
    rewards = list()
    rewards.append(4) # reward at 0 episoades
    for episode in range(1, 1000000): # 1 million episodes are played
        p = 1
        round = 0
        euro = 4
        while euro >= 2 and stopWhen > round: #The number of states differs in every episode
            euro -= 2
            round += 1
            if random.random() < p:
                p -= 0.1 * random.random()
                euro += 3
        rewards.append(euro)
    return sum(rewards)/len(rewards)


def plotExpectedReturns():

    fig = plt.figure()
    plt.title("Expected Reward")
    plt.xlabel("Rounds")
    plt.ylabel("Average Reward (Euro)")
    plt.xlim([0, 30])
    plt.ylim([0, 9])
    allReturns = [(avgReturnsAt(i)) for i in range(0, 31)]
    # plt.plot([max(allReturns) for i in range(0,31)], color="grey") # max reward
    plt.plot([allReturns.index(max(allReturns)), allReturns.index(max(allReturns))],[0, max(allReturns)], color="grey") # optimal num. rounds
    plt.plot(allReturns, color="black")
    print(f"Max Reward: {max(allReturns)}")
    print(f"Optimal Number of Rounds: {allReturns.index(max(allReturns))}")
    plt.show()


def plotmonteCarloLearning():
    iterations = 1000
    curve = [monteCarloLearning() for i in range(0, iterations)]

    fig = plt.figure()
    plt.suptitle("Fitness Curve Monte Carlo Learning", fontsize=18) # title
    plt.title("for 1000 iterations", fontsize=10) # subtitle

    plt.xlabel("Episodes")
    plt.ylabel("Return (Rounds)")
    avgCurve = None
    for c in curve:
        plt.plot(c, color="grey")
        if avgCurve is None: avgCurve = c
    else:
        for i in range(0, len(avgCurve)): avgCurve[i] =+ c[i]

    plt.plot(avgCurve, color="black")
    print(f"Monte Carlo Learning: {avgCurve[iterations-1]}")
    plt.show()


def main():
    print(f"Simple Monte Carlo Method: {monteCarloSimple()}")

    # plotExpectedReturns()

    plotmonteCarloLearning()






if __name__ == '__main__':
    main()
