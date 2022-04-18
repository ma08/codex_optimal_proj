
from collections import Counter

card_ranks = [card[0] for card in input().split()]

result = 0

for rank, count in Counter(card_ranks).items():
    result = max(result, count)

print(result)
