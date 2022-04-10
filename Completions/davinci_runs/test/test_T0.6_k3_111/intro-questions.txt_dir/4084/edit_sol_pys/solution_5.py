
def balls(n, a, b):
    return (n - 1) // (a + b) * a + min(a, (n - 1) % (a + b) + 1)


if __name__ == "__main__":
    n, a, b = map(int, input().split())
    print(balls(n, a, b))
