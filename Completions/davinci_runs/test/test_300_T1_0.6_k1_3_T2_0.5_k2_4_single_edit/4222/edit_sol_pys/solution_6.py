
N, K = map(int, input().split())

has_snack = [0] * N
for i in range(K):
    d_i = int(input())
    for A_i in map(int, input().split()):
        has_snack[A_i - 1] += 1

print(sum(1 for _ in has_snack if _ == 0))
