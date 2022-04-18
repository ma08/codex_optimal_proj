n = int(input())
a = list(map(str, input().split()))
a.sort()
for i in a:
    print(i, end=' ')
