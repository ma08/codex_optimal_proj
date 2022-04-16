

from collections import Counter

hand = input().split()
strength = max(Counter(hand).values())  # .values() returns a list of values in the dict
print(strength)  # prints the max value in the list
