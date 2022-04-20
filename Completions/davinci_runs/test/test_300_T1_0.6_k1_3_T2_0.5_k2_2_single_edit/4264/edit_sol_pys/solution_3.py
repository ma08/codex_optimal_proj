

N = int(input())

if N < 1 or N > 10**5:
    print("invalid input")

# 1, 11, 111, 1111, 11111
length = len(str(N))

# 9
if length % 2 == 1:
    ans = 10 ** (length // 2) - 1
else:
    ans = 10 ** (length // 2) - 1 + N - 10 ** (length - 1) + 1

print(ans)
