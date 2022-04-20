

N, M = map(int, input().split())
A = list(map(int, input().split()))

if max(A) >= 4 * M:
    print("No")
else:
    print("Yes")