
#

N = int(input())
p = list(map(int, input().split()))

for i in range(N):
    if i + 1 == p[i]:
        continue
    else:
        if i + 1 == p[p[i] - 1]:
            print("YES")
            exit()

print("NO")
