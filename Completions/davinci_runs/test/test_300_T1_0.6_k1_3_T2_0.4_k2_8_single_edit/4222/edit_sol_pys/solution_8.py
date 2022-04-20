

N, K = map(int, input().split())

has_snack = [False] * N
for i in range(K):
    d_i = int(input())
    for A_i in map(int, input().split()):
        has_snack[A_i-1] = True

print(sum(1 for x in has_snack if x == 0))
