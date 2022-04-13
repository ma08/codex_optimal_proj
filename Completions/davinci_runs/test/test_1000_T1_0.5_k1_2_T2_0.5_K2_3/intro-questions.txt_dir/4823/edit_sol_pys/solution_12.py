from collections import Counter
ranks = [card[0] for card in input().split()]  # принимаем входные данные

result = 0

for rank, count in Counter(ranks).items():  # подсчитываем количество карт одной масти
    if count > result:
        result = count

print(result)
