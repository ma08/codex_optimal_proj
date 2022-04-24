
N = int(input())

# 9, 99, 999, 9999, 99999
length = len(str(N))

# 1
if length % 2 == 1:
    ans = 10 ** (length // 2) - 1
else:
    ans = 10 ** (length // 2) - 1 + N - 10 ** (length - 1) + 1

print(ans)
