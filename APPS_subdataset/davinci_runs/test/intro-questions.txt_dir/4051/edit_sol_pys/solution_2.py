
def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    for i in range(n):
        if i + 1 < n:
            if a[i] > a[i + 1] + 1:
                print("NO")
                exit()
    print("YES")


if __name__ == '__main__':
    main()
