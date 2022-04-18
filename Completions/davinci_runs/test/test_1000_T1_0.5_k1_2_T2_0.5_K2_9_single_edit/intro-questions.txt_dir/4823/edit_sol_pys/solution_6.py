from collections import Counter

hand = input().split()
strength = max(Counter(hand).values())
print(strength)
