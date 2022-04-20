
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:m]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                print(a[i], end=" ")
    print()

if __name__ == "__main__":
    main()
