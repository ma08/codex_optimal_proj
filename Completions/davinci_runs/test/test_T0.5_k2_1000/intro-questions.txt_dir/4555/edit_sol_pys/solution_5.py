

def main():
    a, b, k = map(int, input().split())
    x = sorted(range(a, b + 1))
    print(*x[:k], sep='\n')  # first k elements
    print(*x[-k:], sep='\n')  # last k elements


if __name__ == '__main__':
    main()
