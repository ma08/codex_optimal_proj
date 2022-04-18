
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += b[a[i] - 1]
        if a[i] == i + 1 and i != n - 1:
            ans += c[i]
    print(ans)

if __name__ == '__main__':
    main()
