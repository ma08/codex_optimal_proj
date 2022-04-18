# https://abc001.contest.atcoder.jp/tasks/abc001_1

# input

N = int(input())

# process
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

alice_sum = 0
bob_sum = 0

for i in range(N):
    if i % 2 == 0:
        alice_sum += A[i]
    else:
        bob_sum += A[i]
# output

print(alice_sum - bob_sum)
