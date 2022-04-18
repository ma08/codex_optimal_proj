

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    faves = list(map(int, sys.stdin.readline().split()))
    joy = list(map(int, sys.stdin.readline().split()))

    fave_cards = {}
    for i, f in enumerate(faves):
        if f in fave_cards:
            fave_cards[f].append(i)
        else:
            fave_cards[f] = [i]

    fave_cards_count = {}
    for f, c in fave_cards.items():
        fave_cards_count[f] = 0

    for c in cards:
        if c in fave_cards:
            fave_cards_count[c] += 1

    cards_per_player = {}
    for f, c in fave_cards.items():
        cards_per_player[f] = fave_cards_count[f] // len(c)

    joy_sum = 0
    for f, c in fave_cards.items():
        joy_sum += joy[cards_per_player[f]] * len(c)

    print(joy_sum)


if __name__ == '__main__':
    main()
