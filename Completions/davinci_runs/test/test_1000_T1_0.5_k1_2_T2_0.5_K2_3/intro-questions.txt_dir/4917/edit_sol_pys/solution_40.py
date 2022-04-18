
def solve(n):
    if n == 0:
        return "INSOMNIA"
    seen = set()
    i = 1
    while len(seen) < 10:
        seen.update(str(i * n))
        i += 1
    return str((i - 1) * n)
