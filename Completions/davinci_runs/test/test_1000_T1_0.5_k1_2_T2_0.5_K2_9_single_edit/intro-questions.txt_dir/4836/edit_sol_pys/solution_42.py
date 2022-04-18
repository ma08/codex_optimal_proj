

def main():
    n, y = map(int, input().split())

    for i in range(n + 1):
        for j in range(n + 1):
            k = n - i - j

            if k < 0:
                continue

            total = 10000 * i + 5000 * j + 1000 * k

            if total == y:
                print(i, j, k)
                return

    print(-1, -1, -1)

if __name__ == "__main__":
    main()
