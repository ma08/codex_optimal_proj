

n, x = map(int, input().split())
a = list(map(int, input().split()))

if x in a:
    print(a.count(x))
else:
    print(0)
