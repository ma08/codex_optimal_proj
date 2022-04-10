

n = int(input())
a = input()
f = list(map(int, input().split()))

s = 0
for i in range(1, n + 1):
    s += f[int(a[-i]) - 1] * 10 ** (i - 1)
print(s)