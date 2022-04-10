

x, k, d = map(int, input().split())

# if x is within k*d distance of 0, the answer is always x-k*d
if abs(x) <= k*d:
    print(abs(x - k*d))
    exit()

# if x is outside k*d distance of 0, the answer is always x%d
print(x % d)