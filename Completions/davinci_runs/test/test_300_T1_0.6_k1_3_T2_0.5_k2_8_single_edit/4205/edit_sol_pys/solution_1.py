
N = int(input())
p = list(map(int, input().split()))

if p == sorted(p):
    print("YES")
else:
    print("NO")
