N, K = map(int, input().split())
snacks = [0] * N
for i in range(K):
    d_i = int(input())
    for A_i in map(int, input().split()):
        snacks[A_i-1] += 1


print(sum(1 for x in snacks if x == 0))
