

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    cards = map(int, sys.stdin.readline().split())
    faves = map(int, sys.stdin.readline().split())
    joy = map(int, sys.stdin.readline().split())

    fav_cards = {}
    for i, f in enumerate(faves):
        if f in fav_cards:
            fav_cards[f].append(i)
        else:
            fav_cards[f] = [i+1]

    fav_cards_count = {}
    for f, c in fav_cards.items():
        fav_cards_count[f] = len(c)

    for c in cards:
        if c in fav_cards_count:
            fav_cards_count[c] -= 1

    cards_per_player = [0] * n
    for c, v in fav_cards_count.items():
        cards_per_player[c-1] = v

    joy_sum = 0
    for i, c in enumerate(cards_per_player):
        joy_sum += joy[c] * fav_cards[i+1]

    print(joy_sum)


if __name__ == '__main__':
    main()
