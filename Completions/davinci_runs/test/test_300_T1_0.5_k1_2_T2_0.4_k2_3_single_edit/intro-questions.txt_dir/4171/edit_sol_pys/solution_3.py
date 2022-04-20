
# Solution

n, k = map(int, input().split())  # n: number of elements, k: number of operations
a = list(map(int, input().split()))  # elements

if k == 1:
    print(max(a))
else:
    print(max(a) - min(a) + 1)
