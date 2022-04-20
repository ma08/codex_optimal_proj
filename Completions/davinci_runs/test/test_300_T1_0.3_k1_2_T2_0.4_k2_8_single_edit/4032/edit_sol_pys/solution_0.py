n, k = map(int, input().split())
a = list(map(int, input().split()))


print(len([x for x in a if x <= k]))
