
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    cards = map(int, sys.stdin.readline().split())
    favs = map(int, sys.stdin.readline().split())
    joy = map(int, sys.stdin.readline().split())

    fav_cards = [[] for _ in range(k)]
    for i, f in enumerate(favs): fav_cards[f - 1].append(i)

    fav_cards_count = [0 for _ in range(k)]
    for c in cards: fav_cards_count[c - 1] += 1

    cards_per_player = [0 for _ in range(k)]
    for i, f in enumerate(fav_cards): cards_per_player[i] = fav_cards_count[i] // len(f)

    print(sum(joy[cards_per_player[f]] * len(f) for f in fav_cards))


if __name__ == '__main__':
    main()
