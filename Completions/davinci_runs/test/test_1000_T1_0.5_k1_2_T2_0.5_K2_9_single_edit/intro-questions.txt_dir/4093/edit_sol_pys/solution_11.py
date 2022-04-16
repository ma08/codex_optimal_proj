

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(max(2 * m - n, n - 2 * m))

if __name__ == '__main__':
    main()
