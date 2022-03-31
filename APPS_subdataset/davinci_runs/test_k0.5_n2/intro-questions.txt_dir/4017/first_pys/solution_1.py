

n = int(input())
a = list(map(int, input().split()))
s = sum(a)
d = {}
for i in range(n):
    d[i+1] = s - a[i]
d = {key:val for key,val in d.items() if val == a[key-1]}
print(len(d))
if len(d) > 0:
    print(*d.keys())