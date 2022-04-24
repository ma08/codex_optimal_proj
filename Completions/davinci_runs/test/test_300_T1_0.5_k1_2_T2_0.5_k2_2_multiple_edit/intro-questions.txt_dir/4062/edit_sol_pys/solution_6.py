def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i):
            ans = max(ans, a[i] ^ a[j])
    print(ans)


# def main():
#     a, b, c, d = map(int, input().split())
#     print(max(a * c, a * d, b * c, b * d))

if __name__ == '__main__':
    main()
