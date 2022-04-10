
n = int(input())
a = list(map(int, input().split()))

if max(a) - min(a) > 1:
    print("NO")
else:
    print("YES")