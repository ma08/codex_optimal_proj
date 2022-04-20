

n, k = map(int, input().split())

victim_list = []
snack_list = []

for _ in range(k):
    d = int(input())
    snack_list.append(set(map(int, input().split())))

print(snack_list)

for i in range(1, n+1):
    flag = True
    for j in range(k):
        if i in snack_list[j]:
            flag = False
            break
    if flag:
        victim_list.append(i)

print(victim_list)

print(len(victim_list))
