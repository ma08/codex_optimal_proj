


def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += c[x[i]-1]
    print(ans)


if __name__ == '__main__':
    main()
