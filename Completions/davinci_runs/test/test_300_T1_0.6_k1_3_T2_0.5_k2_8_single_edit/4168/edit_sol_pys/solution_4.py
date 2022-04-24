
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

# -2の0乗～31乗のリスト
pow_minus2 = [1]
for i in range(1, 32):
    pow_minus2.append(pow_minus2[i - 1] * -2)

# -2の0乗～31乗の累積和
cum_pow_minus2 = [0]
for i in range(1, 32):
    cum_pow_minus2.append(cum_pow_minus2[i - 1] + pow_minus2[i])

ans = ""
for i in range(31):
    if n > 0:
        if cum_pow_minus2[i] <= n and n < cum_pow_minus2[i + 1]:
            ans = "1" + ans
            n -= pow_minus2[i]
        else:
            ans = "0" + ans
    else:
        if cum_pow_minus2[i + 1] <= n and n < cum_pow_minus2[i]:
            ans = "1" + ans
            n -= pow_minus2[i]
        else:
            ans = "0" + ans

if ans == "":
    print(0)
else:
    print(ans)
