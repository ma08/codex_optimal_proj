

N, A, B = map(int, input().split())

b_div_a = N // A
b_mod_a = N % A

if  b_mod_a < A - B:
    ans = b_div_a * A + b_mod_a
else:
    ans = b_div_a * A + A - B

print(ans)
