

n = int(input())
a = list(map(int, input().split()))
if len(a) == 1:
    print(0)
else:
    print(max(a) - min(a) - 1)
