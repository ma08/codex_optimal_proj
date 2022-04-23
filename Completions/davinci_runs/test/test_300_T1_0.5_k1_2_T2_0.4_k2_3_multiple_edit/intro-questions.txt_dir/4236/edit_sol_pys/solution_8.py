

n, m = map(int, input().split())

l = [0] * (m + 1)
r = [0] * (m + 1)

for i in range(n):
    a, b = map(int, input().split())
    l[l] += 1
    r[r] += 1

counter = 0
for i in range(1, m + 1):
    if l[i] == r[i]:
        counter += 1
    elif l[i] > r[i]:
        print(counter)
        break
else:
    print(counter)
