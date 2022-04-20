
# A = 3, B = 4
N, A, B = map(int, input().split())

# c = gcd(A, B)
# lcm = A * B / c
# k = N // lcm
# ans = A * k + min(N % lcm, A)

# print(ans)

b_div_a = N // A
b_mod_a = N % A

if b_mod_a < A - B:
    ans = b_div_a * A + b_mod_a
else:
    ans = b_div_a * A + A - B

print(ans)
