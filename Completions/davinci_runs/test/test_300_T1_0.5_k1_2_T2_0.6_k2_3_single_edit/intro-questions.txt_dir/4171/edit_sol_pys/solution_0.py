

# Solution

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(max(a))
else:

# test
    print(max(a) - min(a) + 1)
