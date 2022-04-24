

def main():
    n, l = map(int, input().split()) # n: 人数, l: 枝
    print((n - 1) * (n) // 2 + n * l)

if __name__ == '__main__':
    main()
