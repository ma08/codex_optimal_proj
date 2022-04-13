def whoServes(n, p, q):
    if (p + q) % 2 == 0:
        return 'paul' if (p + q) % (2 * n) < n else 'opponent'
    return 'opponent' if (p + q) % (2 * n) < n else 'paul'

n, p, q = map(int, input().split())
print(whoServes(n, p, q))
