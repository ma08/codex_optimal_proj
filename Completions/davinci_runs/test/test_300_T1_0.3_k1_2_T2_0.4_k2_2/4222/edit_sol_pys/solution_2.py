

n, k = map(int, input().split())

snack_list = []

for _ in range(k):
    d = int(input())
    snack_list.append(list(map(int, input().split()))[:d])

# print(snack_list)

victim_list = []

for i in range(1, n+1):
    victim_list.append(i)

# print(victim_list)

for i in range(k):
    for j in range(len(victim_list)):
        if victim_list[j] in snack_list[i]:
            victim_list[j] = 0

victim_list = [x for x in victim_list if x != 0]

print(len(victim_list))
