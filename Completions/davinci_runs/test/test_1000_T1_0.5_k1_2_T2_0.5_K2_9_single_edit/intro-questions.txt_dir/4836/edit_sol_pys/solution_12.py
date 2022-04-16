#-----main-----
def get_fruits_count(fruits, c):
    eaten = set()
    cur_sum = 0
    for fruit in fruits:
        if fruit + cur_sum <= c and fruit not in eaten:
            eaten.add(fruit)
            cur_sum += fruit


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
