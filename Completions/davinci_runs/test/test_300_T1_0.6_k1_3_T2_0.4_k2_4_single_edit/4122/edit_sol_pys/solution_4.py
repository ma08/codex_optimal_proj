
H, n = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

for i in range(n):
    H -= A[i]
    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)
