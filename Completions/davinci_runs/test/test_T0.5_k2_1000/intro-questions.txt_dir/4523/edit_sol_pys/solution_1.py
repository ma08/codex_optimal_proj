def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))[:n]
        a.sort()
        print(a[k-1])

if __name__ == "__main__":
    main()
