

# TODO:
# 1. fix syntax errors
# 2. fix logic error

# input:
# 4
# Russia 2000
# Russia 2001
# Russia 2002
# Russia 2003
# 2
# Russia 1
# Russia 2

# output:
# 2001
# 2002

# SOLUTION

n = int(input())

d = {}

for i in range(n):
    country, year = input().split(' ')
    year = int(year)
    if country not in d:
        d[country] = []
    d[country].append(year)

q = int(input())

for i in range(q):
    country, k = input().split(' ')
    k = int(k)
    print(d[country][k-1])
