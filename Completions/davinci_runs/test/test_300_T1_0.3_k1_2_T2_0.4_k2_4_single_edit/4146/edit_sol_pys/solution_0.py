

n = int(input())
v = list(map(int, input().split()))

count = 0
for i in range(n - 1):
    if v[i] == v[i + 1]:
        count += 1

if count == 0:
    print(2)
else:
    print(1)
