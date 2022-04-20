

def find_max_min(n, k):
    a = list(map(int, input().split()))
    # Sort the array
    a.sort()

# Sort the array
a.sort()

# If k is 1, the output is 0
if k == 1:
    print(0)

# If k is n, the output is the difference between the max and min
elif k == n:
    print(a[n - 1] - a[0])

# Otherwise, for each i in range(k, n), get the difference between the max and min
# and then find the minimum of all of those differences
else:
    min_diffs = []

    for i in range(k - 1, n):
        min_diffs.append(a[i] - a[i - k + 1])

    print(min(min_diffs))
