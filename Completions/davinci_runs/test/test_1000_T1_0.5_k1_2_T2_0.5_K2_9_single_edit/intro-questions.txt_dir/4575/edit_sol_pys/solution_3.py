
n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]

for i in a:
    for j in range(d):
        if (j+1) % (i+1) == 0:
            x += 1

print(x)
