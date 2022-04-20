

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p = [0, 0, 0]
for i in range(n):
    if a[i%3] > b[i%3]:
        p[0] += 1
    elif a[i%3] < b[i%3]:
        p[2] += 1
    else:
        p[1] += 1

print(p[0], p[0]+p[1])