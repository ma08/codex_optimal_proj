

from collections import Counter

hand = input().split()
strength = max(Counter(hand).values()) # Counter is a dict subclass for counting hashable objects.
print(strength)
