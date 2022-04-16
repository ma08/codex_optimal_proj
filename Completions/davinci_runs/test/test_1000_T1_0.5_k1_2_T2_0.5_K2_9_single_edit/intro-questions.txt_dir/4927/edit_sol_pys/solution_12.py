

# SOLUTION

def whoServes(n, p, q):
    if p + q == 0:
        return 'paul'
    elif (p + q) % (2 * n) < n:
        if (p + q) % 2 == 0:
            return 'paul'
        else:
            return 'opponent'
    else:
        if (p + q) % 2 == 0:
            return 'opponent'
        else:
            return 'paul'


def main():
    n, p, q = map(int, input().split())
    print(whoServes(n, p, q))


if __name__ == "__main__":
    main()
