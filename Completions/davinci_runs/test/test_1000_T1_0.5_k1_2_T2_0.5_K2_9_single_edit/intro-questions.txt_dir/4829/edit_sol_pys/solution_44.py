

def main(n, a, b):
    if a == b:
        print(0)
        return
    if a > b:
        a, b = b, a
    if n % (a + b) == 0:
        print(n // (a + b))
        return
    if n % (a + b) <= a:
        print(n // (a + b))
        return
    else:
        print(n // (a + b) + 1)
        return

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    main(n, a, b)
