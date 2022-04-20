

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] % 2 == 0 and A[i] % 3 != 0 and A[i] % 5 != 0:
        print("DENIED")
        break
else:
    print("APPROVED")