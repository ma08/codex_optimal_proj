

########## SOLUTION ##########

n = int(input())

d = list(map(int, input().split()))  # list of distances

l = [0] * n  # list of positions

l[0] = 1  # first position is 1

for i in range(1, n):
    l[i] = l[i-1] + d[i-1] + 1  # current position is previous position plus distance to previous position plus 1

print(*l)
