from collections import Counter

ranks = [card[0] for card in input().split() if card[0] in '23456789TJQKA']

result = 0

for rank, count in Counter(ranks).items():
    if count > result:
        result = count

print(result)
