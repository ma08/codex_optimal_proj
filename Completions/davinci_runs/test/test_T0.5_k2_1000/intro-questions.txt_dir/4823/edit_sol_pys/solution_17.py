

from collections import Counter

n = int(input())

for i in range(n):
    hand = input().split()
    strength = max(Counter(hand).values())
    print(strength)
