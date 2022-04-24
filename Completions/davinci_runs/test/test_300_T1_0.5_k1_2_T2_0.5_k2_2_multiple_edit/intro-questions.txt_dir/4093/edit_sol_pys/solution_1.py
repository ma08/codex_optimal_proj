
def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if m == 1:
            print(0)
        else:
            print(max(2 * m - n, n - 2 * (m - 1)))

if __name__ == '__main__':
    main()
