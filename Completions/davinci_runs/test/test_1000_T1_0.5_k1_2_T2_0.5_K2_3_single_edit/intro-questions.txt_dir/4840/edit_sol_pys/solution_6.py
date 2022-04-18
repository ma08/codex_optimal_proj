

import numpy as np
from scipy.stats import binom

def prob_distr(a, b):
    """
    Finds the probability of each outcome occurring
    in a given range of numbers.
    """
    distr = [1/(b-a+1) for i in range(a, b+1)]
    return np.array(distr)

def find_prob(distr1, distr2):
    """
    Finds the probability of each possible outcome
    of the sum of the two dice.
    """
    prob = [distr1[i]*distr2[j] for i in range(len(distr1)) for j in range(len(distr2))]
    return np.array(prob)

def find_winner(prob1, prob2):
    """
    Finds the probability of each player winning
    and decides who has the higher probability of winning.
    """
    prob_gunnar = np.sum(prob1[:int(len(prob1)/2)])
    prob_emma = np.sum(prob2[:int(len(prob2)/2)])
    return "Gunnar" if prob_gunnar > prob_emma else "Emma" if prob_gunnar < prob_emma else "Tie"

def main():
    gunnar_dice = input().split()
    gunnar_dice = [int(i) for i in gunnar_dice]
    emma_dice = input().split()
    emma_dice = [int(i) for i in emma_dice]

    gunnar_distr = prob_distr(gunnar_dice[0], gunnar_dice[1])
    emma_distr = prob_distr(emma_dice[0], emma_dice[1])

    gunnar_prob = find_prob(gunnar_distr, gunnar_distr)
    emma_prob = find_prob(emma_distr, emma_distr)

    print(find_winner(gunnar_prob, emma_prob))

if __name__ == "__main__":
    main()
