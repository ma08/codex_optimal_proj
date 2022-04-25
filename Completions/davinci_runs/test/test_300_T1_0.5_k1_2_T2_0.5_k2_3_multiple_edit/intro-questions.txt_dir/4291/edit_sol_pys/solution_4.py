def main():
    n, m = map(int, input().split())
    s = input().split()
    lr = [list(map(int, input().split())) for _ in range(m)]
    ans = []
    for i in range(m):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
