
def get_digit(s, k):
    if k <= len(s):
        return s[k-1]
    for i, c in enumerate(s):
        k -= (int(c) * (10 ** (i + 1)))
        if k <= 0:
            return str(int(c))[-1:]
