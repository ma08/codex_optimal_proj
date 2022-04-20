

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    a.sort()
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (i+1))
    print(ans)


if __name__ == '__main__':
    main()
