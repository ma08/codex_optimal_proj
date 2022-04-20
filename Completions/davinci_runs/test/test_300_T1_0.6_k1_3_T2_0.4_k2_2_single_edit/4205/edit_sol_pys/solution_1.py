
N = int(input())
P = list(map(int, input().split()))

for i in range(N):
    if i + 1 == P[i]:
        continue
    else:
        if i + 1 == P[P[i] - 1]:
            print("YES")
            exit()

print("NO")
