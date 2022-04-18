# coding: utf-8

import sys

def main():
    n = int(input())
    cards = {}
    for i in range(n):
        k = int(input())
        cards[i] = []
        for j in range(k):
            cost, damage = [int(x) for x in input().split()]
            cards[i].append((cost, damage))
    damage = 0
    for i in range(n):
        cards[i].sort(key=lambda x: x[1], reverse=True)
        cost = 0
        damage = 0
        for card in cards[i]:
            if cost + card[0] <= 3:
                cost += card[0]
                if cost % 10 == 0:
                    damage += card[1] * 2
                else:
                    damage += card[1]
    print(damage)

if __name__ == "__main__":
    main()
