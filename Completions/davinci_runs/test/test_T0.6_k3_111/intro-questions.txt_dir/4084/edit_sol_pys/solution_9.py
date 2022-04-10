
def ball(n, a, b):
    if (a == 0 and b == 0) or n == 0:
        return 0
    else:
        return (n - 1) // (a + b) * a + min(a, (n - 1) % (a + b) + 1)


if __name__ == "__main__":
    n, a, b = map(int, input().split())
    print(ball(n, a, b))
