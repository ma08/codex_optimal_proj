

from collections import Counter

ranks = [card[0] for card in input().split()]  # получаем список из мастей карт

result = 0

for rank, count in Counter(ranks).items():  # получаем список из количества карт каждой масти
    if count > result:
        result = count

print(result)
