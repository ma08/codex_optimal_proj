

def main():
    n, m, a = map(int, input().split())
    if n % a == 0:
        n = n // a
    else:
        n = n // a + 1
    if m % a == 0:
        m = m // a
    else:
        m = m // a + 1
    print(n * m)

if __name__ == "__main__":
    main()
