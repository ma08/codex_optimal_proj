

n = int(input())
v = list(map(int, input().split()))

count = {}

for i in range(n):
    if v[i] not in count:
        count[v[i]] = 1
    else:
        count[v[i]] += 1

if len(count) != 2:
    print(-1)
    exit()

key = list(count.keys())

if count[key[0]] != count[key[1]]:
    print(-1)
    exit()

ans = 0

for i in range(n-2):
    if v[i] != v[i+2]:
        ans += 1

print(ans)