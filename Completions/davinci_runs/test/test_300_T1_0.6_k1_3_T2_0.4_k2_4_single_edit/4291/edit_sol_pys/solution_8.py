# ABC081A - Placing Marbles

n, q = map(int, input().split())
s = input()

l_r_list = []
for i in range(q):
    l_r = list(map(int, input().split()))
    l_r_list.append(l_r)

counts = 0
count_list = []

for i in range(n - 1):
    if s[i] == "A" and s[i + 1] == "C":
        counts += 1
    count_list.append(counts)

for l_r in l_r_list:
    l = l_r[0] - 1
    r = l_r[1] - 2
    if l == 0:
        print(count_list[r])
    else:
        print(count_list[r] - count_list[l - 1])
