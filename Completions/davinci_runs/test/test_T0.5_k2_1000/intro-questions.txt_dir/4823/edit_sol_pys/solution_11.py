

from collections import Counter

hand = input().split()  # input the hand
strength = max(Counter(hand).values())  # find the strength of the hand
print(strength)  # print the strength
