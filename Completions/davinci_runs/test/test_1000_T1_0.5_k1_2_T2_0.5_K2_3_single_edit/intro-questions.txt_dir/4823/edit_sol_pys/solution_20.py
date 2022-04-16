

from collections import Counter

ranks = [card[0] for card in input().split()]  # присваиваем список из рангов карт

result = 0  # переменная для вывода результата

for rank, count in Counter(ranks).items():  # для каждого ранга в списке рангов
    if count > result:
        result = count

print(result)
