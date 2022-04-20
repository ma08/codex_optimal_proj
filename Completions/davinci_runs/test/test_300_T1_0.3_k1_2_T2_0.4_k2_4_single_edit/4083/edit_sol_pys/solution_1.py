

n, k = map(int, input().split()) # n: number of elements, k: number of operations
a = list(map(int, input().split())) # a: list of elements

a.sort()

if a[0] == a[-1]:
    print(0)
else:
    print(a[-1] - a[0] + 1)
