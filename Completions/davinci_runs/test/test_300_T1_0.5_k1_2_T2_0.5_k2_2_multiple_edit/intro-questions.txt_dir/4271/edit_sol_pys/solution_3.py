n = int(input())
dishes = list(map(int, input().split())) # типы блюд
points = list(map(int, input().split())) # цены блюд
bonus = list(map(int, input().split())) # бонусы за соседние блюда

ans = 0
for i in range(n):
    ans += points[dishes[i] - 1] # прибавляем цену текущего блюда
    if i > 0 and dishes[i] == dishes[i - 1] + 1: # если мы не на первом блюде и текущее блюдо соседнее с предыдущим
        ans += bonus[dishes[i - 1] - 1] # прибавляем бонус

print(ans)
