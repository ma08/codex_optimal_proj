def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    res = 0
    for i in range(n):
        res += max(a[i], b[i])

    print(res)

if __name__ == "__main__":
    main()
