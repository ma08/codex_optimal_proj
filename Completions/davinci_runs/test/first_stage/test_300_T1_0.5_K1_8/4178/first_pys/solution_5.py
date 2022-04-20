


def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(1, n):
        if h[i] < h[i-1]:
            h[i] = h[i-1]
    print("Yes" if all(h[i] <= h[i+1] for i in range(n-1)) else "No")


if __name__ == '__main__':
    main()