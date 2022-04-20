


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if sorted(s[i]) == sorted(s[j]):
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()