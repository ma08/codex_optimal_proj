

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    favs = list(map(int, sys.stdin.readline().split()))
    joy = list(map(int, sys.stdin.readline().split()))

    fav_cards_per_player = {}
    for i, f in enumerate(favs):
        if f in fav_cards_per_player:
            fav_cards_per_player[f].append(i)
        else:
            fav_cards_per_player[f] = [i]

    fav_cards_count = {}
    for f, c in fav_cards_per_player.items():
        fav_cards_count[f] = 0

    for c in cards:
        if c in fav_cards_per_player:
            fav_cards_count[c] += 1

    cards_per_player = {}
    for f, c in fav_cards_per_player.items():
        cards_per_player[f] = fav_cards_count[f] // len(c)

    joy_sum = 0
    for f, c in fav_cards_per_player.items():
        joy_sum += joy[cards_per_player[f]] * len(c)

    print(joy_sum)


if __name__ == '__main__':
    main()
