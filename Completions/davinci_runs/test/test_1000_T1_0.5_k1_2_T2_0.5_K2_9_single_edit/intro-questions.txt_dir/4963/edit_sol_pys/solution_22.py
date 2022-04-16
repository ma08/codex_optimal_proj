

########## SOLUTION ##########
n = int(input())
d = list(map(int, input().split()))
l = [0] * n
l[0] = 1

for i in range(1, n):
    l[i] = l[i-1] + d[i-1] + 1
print(*l)
