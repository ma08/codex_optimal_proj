

n, q = map(int, input().split())
s = input()

l_r_list = []
for i in range(q):
    l_r = list(map(int, input().split()))
    l_r_list.append(l_r)

ac_count = 0
ac_count_list = [0]

for i in range(n - 1):
    if s[i] == "A" and s[i + 1] == "C":
        ac_count += 1
    ac_count_list.append(ac_count)

for l_r in l_r_list:
    l = l_r[0] - 1
    r = l_r[1] - 2
    if l == 0:
        print(ac_count_list[r])
    else:
        print(ac_count_list[r] - ac_count_list[l - 1])
