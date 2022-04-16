
def reverse(t):
    n = len(t)
    for i in reversed(range(1, n + 1)):
        if n % i == 0:
            # reverse the substring
            t = t[:i][::-1] + t[i:]
    return t
