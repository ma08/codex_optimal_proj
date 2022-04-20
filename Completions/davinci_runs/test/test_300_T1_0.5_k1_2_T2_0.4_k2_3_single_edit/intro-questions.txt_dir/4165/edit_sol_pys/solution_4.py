N = int(input())
A = list(map(int, input().split()))


A.sort()

if A[0] + A[1] > A[-1]:
    print("Yes")
else:
    print("No")
