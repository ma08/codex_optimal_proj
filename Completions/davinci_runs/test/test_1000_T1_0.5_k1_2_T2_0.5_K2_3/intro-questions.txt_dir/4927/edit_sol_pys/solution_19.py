
# SOLUTION

def whoServes(n, p, q):
    if (p + q) % (2 * n) < n:
        return 'paul' if (p + q) % 2 == 0 else 'opponent'
    else:
        return 'opponent' if (p + q) % 2 == 0 else 'paul'

n, p, q = map(int, input().split())
print(whoServes(n, p, q))
