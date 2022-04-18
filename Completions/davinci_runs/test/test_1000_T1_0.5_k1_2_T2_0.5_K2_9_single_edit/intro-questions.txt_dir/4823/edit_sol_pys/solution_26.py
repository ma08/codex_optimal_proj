

from collections import Counter

hand = input().split() 
strength = max(Counter(hand).values()) # counts the number of times each card appears in the hand
print(strength)
