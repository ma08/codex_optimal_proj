

def main():
    a, b, k = map(int, input().split())
    y = range(a, b+1)
    y = sorted(y)
    print(*y[:k])
    print(*y[-k:])

if __name__ == '__main__':
    main()
