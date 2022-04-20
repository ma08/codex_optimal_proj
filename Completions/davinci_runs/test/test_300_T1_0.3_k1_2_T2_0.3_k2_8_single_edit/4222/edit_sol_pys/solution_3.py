

n, k = map(int, input().split())

snack_list = []

for _ in range(k):
    d = int(input())
    snack_list.append(set(map(int, input().split())))

# print(snack_list)

victim_list = []

for i in range(1, n+1):
    victim_list.append(i)

# print(victim_list)

for i in range(1, k):
    for j in snack_list[i]:
        if j in victim_list:
            victim_list.remove(j)

print(len(victim_list))
