

import sys, math

def main():
    # Read input
    n,k,q = map(int,input().split())
    answers = [int(input()) for i in range(q)]

    # Calculate the players' scores after each question
    scores = [k] * n # create a list of k's
    for a in answers:
        scores[a-1] += 1 # add 1 to the answer
        for i in range(n):
            if i != a-1:
                scores[i] -= 1 # subtract 1 from the wrong answer

    # Print whether each player survived the game
    for s in scores: # iterate through the scores
        if s > 0: # if the score is greater than 0
            print("Yes") # print yes
        else: # if the score is less than 0
            print("No") # print no

if __name__ == '__main__':
    main()
