

N = int(input())
p = list(map(int, input().split()))

if p[0] == 1:
    if p[1] == 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")