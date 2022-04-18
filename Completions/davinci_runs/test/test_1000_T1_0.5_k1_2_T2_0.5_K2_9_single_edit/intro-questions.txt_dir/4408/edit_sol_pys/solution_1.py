

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    cards = map(int, sys.stdin.readline().split())
    favs = map(int, sys.stdin.readline().split())
    joy = map(int, sys.stdin.readline().split())

    fav_cards = {}
    for i, f in enumerate(favs):
        if f in fav_cards:
            fav_cards[f].append(i)
        else:
            fav_cards[f] = [i]

    fav_cards_count = {}
    for f in fav_cards:
        fav_cards_count[f] = 0

    for c in cards:
        if c in fav_cards:
            fav_cards_count[c] += 1

    cards_per_player = {}
    for f, c in fav_cards.items():
        cards_per_player[f] = fav_cards_count[f] // len(c)

    joy_sum = 0
    for f in fav_cards:
        joy_sum += joy[cards_per_player[f]] * len(c)

    print(joy_sum)


if __name__ == '__main__':
    main()
