import random

p = 0.4

def monteCarlo():

    rounds = list()
    for episode in range(1, 1000000): # 1 000 000 episodes are played
        round = 0
        euro = 4
        while euro >= 2: #The number of states differs in every episode
            round += 1
            euro -= 2
            if random.random() < p:
                euro += 3

        rounds.append(round)

    return sum(rounds)/len(rounds)  # 4.424012424012424


def exactResult(i):
    if i > 10: return 0
    return (1+1.5*exactResult(i+1))*p  +  2*(1-p)*(1-p) + (2+1.5*exactResult(i+1))*(1-p)*p



if __name__ == '__main__':
    print(f"Monte Carlo Method: {monteCarlo()}")
    print(f"Actual Result: {exactResult(0)}")

