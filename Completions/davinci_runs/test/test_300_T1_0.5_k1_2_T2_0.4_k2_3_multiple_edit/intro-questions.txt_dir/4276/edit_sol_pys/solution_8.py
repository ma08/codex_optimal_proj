# ABC085C
# https://atcoder.jp/contests/abs/tasks/abc085_c

N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N + 1):
        if i + j > N:
            break
        k = N - i - j
        if i * 10000 + j * 5000 + k * 1000 == Y:
            print(i, j, k)
            exit()
print('-1 -1 -1')
