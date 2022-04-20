

n = int(input())
a = list(map(int, input().split()))

if len(set(a)) == 1:
    print("YES")
else:
    print("NO")