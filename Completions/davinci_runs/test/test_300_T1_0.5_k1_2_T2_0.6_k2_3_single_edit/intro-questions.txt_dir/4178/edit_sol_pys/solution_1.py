def main():
    n = int(input())
    d = list(map(int, input().split()))

    d.sort()
    ans = d[-1] - d[0]


    print(ans)


if __name__ == '__main__':
    main()
