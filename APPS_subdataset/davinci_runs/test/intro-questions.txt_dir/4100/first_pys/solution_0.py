

import sys

def main():
    # Read input
    n,k,q = map(int,sys.stdin.readline().split())
    answers = [int(sys.stdin.readline()) for i in range(q)]

    # Calculate the players' score after each question
    scores = [k] * n
    for a in answers:
        scores[a-1] += 1
        for i in range(n):
            if i != a-1:
                scores[i] -= 1

    # Print whether each player survived the game
    for s in scores:
        if s > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()