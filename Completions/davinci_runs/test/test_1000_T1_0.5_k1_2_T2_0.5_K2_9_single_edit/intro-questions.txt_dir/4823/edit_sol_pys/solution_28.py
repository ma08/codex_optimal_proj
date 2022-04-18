
 
from collections import Counter

ranks = [card[0] for card in input().split()]

result = 0

for rank, count in Counter(ranks).items():
    if count > result:
        result = count

print(result)
