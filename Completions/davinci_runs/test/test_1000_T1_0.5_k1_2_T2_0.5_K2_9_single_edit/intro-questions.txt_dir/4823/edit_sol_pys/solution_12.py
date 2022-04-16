

from collections import Counter

hand = raw_input().split()
strength = max(Counter(hand).values())
print(strength)
