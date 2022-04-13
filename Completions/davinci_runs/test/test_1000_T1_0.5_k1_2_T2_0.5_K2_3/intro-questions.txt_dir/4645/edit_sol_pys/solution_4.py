
def is_valid(p):
    n = len(p)
    for i in range(n-1):
        if abs(p[i] - p[i + 1]) < 2 or abs(p[i] - p[i + 1]) > 5:
            return False
    return True


def permute(n):
    p = list(range(1, n + 1))
    while True:
        if is_valid(p):
            return p

        p = next_permutation(p)

def next_permutation(p):
    n = len(p)
    i = n - 2
    while i >= 0 and p[i] >= p[i + 1]:
        i -= 1
    if i == -1:
        return None
    j = i + 1
    while j < n and p[j] > p[i]:
        j += 1
    j -= 1
    p[i], p[j] = p[j], p[i]
    p[i + 1:] = p[:i:-1]
    return p


t = int(input())
for i in range(t):
    n = int(input())
    p = permute(n)
    if p is None:
        print(-1)
    else:
        print(' '.join(map(str, p)))
