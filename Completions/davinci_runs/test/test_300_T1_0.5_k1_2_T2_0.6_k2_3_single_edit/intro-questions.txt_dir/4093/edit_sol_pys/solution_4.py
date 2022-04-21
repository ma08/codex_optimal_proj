

def main():
    arr = []
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if n == 1:
            arr.append(0)
        else:
            arr.append(max(2 * m - n, n - 2 * m))
    print(*arr)

if __name__ == '__main__':
    main()
