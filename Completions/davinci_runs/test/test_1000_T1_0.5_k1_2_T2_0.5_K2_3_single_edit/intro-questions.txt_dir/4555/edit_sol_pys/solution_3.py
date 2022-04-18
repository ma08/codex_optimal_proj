

def main():
    a, b, k = map(int, input().split())
    x = list(range(a, b+1))
    x = sorted(x)
    print(' '.join(map(str, x[:k])))
    print(' '.join(map(str, x[-k:])))

if __name__ == '__main__':
    main()
