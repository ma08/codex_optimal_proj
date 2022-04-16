#-----input-----
# 3 7
# 3 4 2

#-----main-----
n, c = map(int, input().split())
fruits = list(map(int, input().split()))
eaten = set()
cur_sum = 0
for fruit in fruits:
    if fruit + cur_sum <= c and fruit not in eaten:
        eaten.add(fruit)
        cur_sum += fruit
print(len(eaten))
