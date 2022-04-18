

from collections import Counter
ranks = [cards[0] for cards in input().split()]

result = 0

for rank, count in Counter(ranks).items():
    if count > result:
        result = count

print(result)
