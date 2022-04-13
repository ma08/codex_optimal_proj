

from collections import Counter

n = int(input()) # number of entries
rolls = [int(x) for x in input().split()] # list of rolls

result = Counter(rolls) # count how many times each roll is repeated

print(result)
