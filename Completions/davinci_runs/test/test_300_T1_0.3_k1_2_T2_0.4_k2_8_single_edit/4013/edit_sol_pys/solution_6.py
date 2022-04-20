

n = int(input())
a = list(map(int, input().split()))
if max(a) - min(a) - 1 < 0:
    print(0)
else:
    print(max(a) - min(a) - 1)
