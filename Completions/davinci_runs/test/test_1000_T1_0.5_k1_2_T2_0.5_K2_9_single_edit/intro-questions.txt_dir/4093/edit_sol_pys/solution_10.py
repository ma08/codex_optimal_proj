

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if n == 1:
        elif n == 2:
            print(m)
            print(0)
        else:
            print(max(2 * m - n, n - 2 * m))

if __name__ == '__main__':
    main()
