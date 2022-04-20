

N = int(input())
X = [int(x) for x in input().split()]

ans = sum([(x-X[0])**2 for x in X])

for i in range(1, 101):
    temp = sum([(x-i)**2 for x in X])
    if ans > temp:
        ans = temp

print(ans)