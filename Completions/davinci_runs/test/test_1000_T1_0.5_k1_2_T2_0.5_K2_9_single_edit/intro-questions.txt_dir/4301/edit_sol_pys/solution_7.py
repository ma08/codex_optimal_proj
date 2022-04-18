'''

N = int(input())
A = list(map(int, input().split()))

max_a = max(A)
for a in A:
'''

N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

A.sort(reverse=True)

# print(A)

ans = 0
for i in range(K):
    ans += A[i]

print(ans)
    print(max_a if a != max_a else max(A) - 1)
