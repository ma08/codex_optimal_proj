def get_digit(s, k):
    if k <= len(s):
        return s[k - 1]
    for i, c in enumerate(s):
        k -= (int(c) * (10 ** (i + 1)))
        if k <= 0: return str(int(c))[-1]
s, k = input(), int(input())
print(s if len(s) == 1 else get_digit(s, k))
