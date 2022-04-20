

n = int(input())
v = list(map(int, input().split()))

dic = {}
for i in range(n):
    if v[i] in dic:
        dic[v[i]] += 1
    else:
        dic[v[i]] = 1

if len(dic) == 2:
    if dic[v[0]] == dic[v[1]]:
        print(0)
    else:
        print(1)
else:
    print(2)