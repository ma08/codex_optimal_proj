

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    faves = list(map(int, sys.stdin.readline().split()))
    joy = list(map(int, sys.stdin.readline().split()))

    fave_cards = [[] for _ in range(n)]
    for i, f in enumerate(faves, 1):
        fave_cards[f - 1].append(i)

    fave_cards_count = [0 for _ in range(n)]

    for c in cards:
        fave_cards_count[c - 1] += 1

    cards_per_player = [c // len(f) for c, f in zip(fave_cards_count, fave_cards)]

    joy_sum = 0
    for j, c in zip(joy, cards_per_player):
        joy_sum += j * c

    print(joy_sum)


if __name__ == '__main__':
    main()
