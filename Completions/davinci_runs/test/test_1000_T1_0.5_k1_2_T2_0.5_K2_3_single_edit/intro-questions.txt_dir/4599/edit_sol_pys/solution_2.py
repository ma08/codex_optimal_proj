
N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

alice_sum = 0
bob_sum = 0

for i in range(N):
    if i % 2 == 0:
        alice_sum += A[i]
    else:
        bob_sum += A[i]

print(alice_sum - bob_sum)
