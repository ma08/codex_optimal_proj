

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if n <= m:
            print(0)
        else:
            if n % m == 0:
                print(0)
            else:
                print(m - n % m)


if __name__ == '__main__':
    main()
