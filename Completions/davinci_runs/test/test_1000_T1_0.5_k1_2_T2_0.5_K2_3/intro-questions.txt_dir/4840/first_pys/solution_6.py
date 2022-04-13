

import numpy as np
from scipy.stats import binom

def prob_distr(a, b):
    """
    Finds the probability of each outcome occurring
    in a given range of numbers.
    """
    distr = []
    for i in range(a, b+1):
        distr.append(1/(b-a+1))
    return distr

def find_prob(distr1, distr2):
    """
    Finds the probability of each possible outcome
    of the sum of the two dice.
    """
    prob = []
    for i in range(len(distr1)):
        for j in range(len(distr2)):
            prob.append(distr1[i]*distr2[j])
    return prob

def find_winner(prob1, prob2):
    """
    Finds the probability of each player winning
    and decides who has the higher probability of winning.
    """
    prob_gunnar = 0
    prob_emma = 0
    for i in range(len(prob1)):
        if i < len(prob1)/2:
            prob_gunnar += prob1[i]
        else:
            prob_emma += prob2[i]
    if prob_gunnar > prob_emma:
        return "Gunnar"
    elif prob_gunnar < prob_emma:
        return "Emma"
    else:
        return "Tie"

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