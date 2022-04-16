

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    cards = map(int, sys.stdin.readline().split())
    favs = list(map(int, sys.stdin.readline().split()))
    joy = list(map(int, sys.stdin.readline().split()))

    fav_cards = {}
    for i, f in enumerate(favs):
        if f in fav_cards:
            fav_cards[f].append(i)
        else:
            fav_cards[f] = [i]

    fav_cards_count = {}
    for f, c in fav_cards.items():
        fav_cards_count[f] = len(c)
    print(fav_cards)
    print(fav_cards_count)
    for c in cards:
        if c in fav_cards:
            fav_cards_count[c] += 1

    print(cards_per_player)
    cards_per_player = {}
    for f, c in fav_cards_count.items():
        cards_per_player[f] = fav_cards_count[f] // len(c)

    joy_sum = 0
    for f, c in fav_cards_count.items():
        joy_sum += joy[cards_per_player[f]] * len(c)

    print(joy_sum)


if __name__ == '__main__':
    main()
