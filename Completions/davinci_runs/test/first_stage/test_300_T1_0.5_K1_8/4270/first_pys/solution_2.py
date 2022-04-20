

# input
n = int(input())
v = [int(i) for i in input().split(' ')]

# sort
v.sort()

# loop
for i in range(n-1):
    v[i+1] = (v[i] + v[i+1]) / 2

# print
print(v[-1])