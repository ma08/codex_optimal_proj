

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if n == 1:
            print(0)
        elif m * 2 > n:
            print(m * 2 - n)
        else:

            print(n - 2 * m)

if __name__ == '__main__':
    main()
