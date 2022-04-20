

# a = 2, b = 1, c = 1, k = 3
a, b, c, k = map(int, input().split())

# If a is smaller than k, then use all a
if a < k:
    # If k - a is larger than b + c, then use all b + c
    if k - a > b + c:
        print(a - (k - a - (b + c)))
    # Otherwise, use k - a
    else:
        print(a - (k - a))
# Otherwise, use k
else:
    print(k)