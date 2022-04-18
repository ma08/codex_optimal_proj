
n = int(input())
a = list(map(int,input().split()))

sm = 0
for i in range(n):
    sm += 1/a[i]

print(1/sm)
