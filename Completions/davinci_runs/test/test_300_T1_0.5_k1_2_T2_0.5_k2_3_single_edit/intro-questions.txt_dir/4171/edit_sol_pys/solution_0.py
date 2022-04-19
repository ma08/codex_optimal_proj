
# Get inputs
# Solution

n, k = map(int, input().split())
a = list(map(int, input().split()))
# If k is 1, no need to subtract
if k == 1:
# Otherwise, find the max and min and subtract
    print(max(a))
else:
    print(max(a) - min(a) + 1)
