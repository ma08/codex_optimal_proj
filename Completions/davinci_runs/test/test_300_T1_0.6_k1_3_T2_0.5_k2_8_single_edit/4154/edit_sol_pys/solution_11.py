

import sys


def main():
    n, m = map(int, input().split())
    gates = [list(map(int, input().split())) for _ in range(m)]

    # convert the input to a list of lists that contains the gates allowed by each ID card
    allowed_gates = [[] for _ in range(n)]
    for i in range(m):
        for j in range(gates[i][0] - 1, gates[i][1]):
            allowed_gates[j].append(i)

    # initialize the number of ID cards which allow to pass all the gates alone to 0
    num_cards = 0

    # iterate through the list of lists of allowed gates for each ID card
    for allowed in allowed_gates:
        # find the number of gates which are allowed by only this ID card
        # by finding the difference between the number of allowed gates and the number of gates allowed by all the other ID cards
        num_alone = len(allowed) - \
            len(set(allowed) - set(allowed_gates[0]) - set(allowed_gates[1]) - set(allowed_gates[2]) - set(allowed_gates[3]))
        # if the number of gates alone is equal to the total number of gates, then this ID card allows to pass all the gates alone
        if num_alone == m:
            num_cards += 1

    print(num_cards)


if __name__ == '__main__':
    main()
