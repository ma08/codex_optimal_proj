

from collections import Counter

hand = input().split() #hand is a list of strings, we split the input string into a list of strings
strength = max(Counter(hand).values()) #Counter() is a class that counts the number of occurences of each element in a list

#print(Counter(hand))
print(strength)
