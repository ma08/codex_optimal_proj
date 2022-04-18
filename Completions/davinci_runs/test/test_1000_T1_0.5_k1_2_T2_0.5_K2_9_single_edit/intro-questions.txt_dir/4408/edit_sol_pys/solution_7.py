

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
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

    for c in cards:
        else:
            fav_cards_count[c] = 0
        if c in fav_cards:
            fav_cards_count[c] += 1

    cards_per_player = {}
    for f, c in fav_cards.items():
        cards_per_player[f] = fav_cards_count[f] // len(c)

    joy_sum = 0
    for f, cp in cards_per_player.items():
        joy_sum += joy[cp] * fav_cards_count[f]

    print(joy_sum)


if __name__ == '__main__':
    main()
