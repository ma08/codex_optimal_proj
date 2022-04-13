
n, k = map(int, input().split())
s = input()
d = {'a':0, 'b':0, 'c':0}
for i in range(n):
    d[s[i]] += 1
for i in range(k):
    x = max(d.values())
    for j in d.keys():
        if d[j] == x:
            d[j] -= 1
            print(j, end='')
            break
