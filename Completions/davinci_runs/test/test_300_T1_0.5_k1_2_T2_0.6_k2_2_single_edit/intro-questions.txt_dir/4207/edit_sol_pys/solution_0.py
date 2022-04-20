
N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
    
if A == [0] * N:
    print(0)
    exit()
if B == [0] * N:
    print(N)
    exit()
    
A.sort()
B.sort()
ans = 0
for i in range(N):
    if A[i] * B[N - 1 - i] > 0:
        break
    else:
        ans += 1
print(ans)
