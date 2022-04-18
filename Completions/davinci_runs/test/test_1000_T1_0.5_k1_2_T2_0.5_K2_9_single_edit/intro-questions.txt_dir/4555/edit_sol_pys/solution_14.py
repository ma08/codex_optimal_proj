

def main():
    a, b, k = map(int, input().split())
    x = sorted(range(a, b+1))
    print(*x[:k], *x[-k:])

if __name__ == '__main__':
    main()
