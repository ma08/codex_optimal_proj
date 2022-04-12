# https://atcoder.jp/contests/abc085/tasks/abc085_c

n, y = map(int, input().split())

for i in range(n + 1):
    for j in range(n - i + 1):
        k = n - i - j
        if i * 10000 + j * 5000 + k * 1000 == y:
            print(str(i) + " " + str(j) + " " + str(k))
            exit()

print("-1 -1 -1")
