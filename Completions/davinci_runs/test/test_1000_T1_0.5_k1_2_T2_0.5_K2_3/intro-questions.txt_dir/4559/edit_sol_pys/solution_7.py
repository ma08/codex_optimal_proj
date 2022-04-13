N = int(input())
A = [int(i) for i in input().split()]
res = 1
for i in range(N):
    if A[i] == 0:
        print(0)
        exit()
    res *= A[i] % (10 ** 9 + 7)
print(res % (10 ** 9 + 7))
