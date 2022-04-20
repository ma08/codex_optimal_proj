

n, k = map(int, input().split())

snack_list = []

for _ in range(k):
    d = int(input())
    snack_list.append(list(map(int, input().split()))[1:])

# print(snack_list)

victim_list = []

for i in range(1, n+1):
    if i not in snack_list[0]:
        victim_list.append(i)

# print(victim_list)

for i in range(1, k):
    for j in range(len(victim_list)):
        if victim_list[j] in snack_list[i]:
            victim_list.pop(j)

print(len(victim_list))
