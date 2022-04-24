

n, q = map(int, input().split())
s = input()
l_r_list = [0] * q
for i in range(q):
    l_r = list(map(int, input().split()))
    l_r_list[i] = l_r

ac_counts = 0
ac_count_list = [0] * (n - 1)

for i in range(n-1):
    if s[i] == "A" and s[i + 1] == "C":
        ac_counts += 1
    ac_count_list[i] = ac_counts

for i in range(q):
    l = l_r_list[i][0] - 1
    r = l_r_list[i][1] - 2
    
    print(ac_count_list[r] - ac_count_list[l])
