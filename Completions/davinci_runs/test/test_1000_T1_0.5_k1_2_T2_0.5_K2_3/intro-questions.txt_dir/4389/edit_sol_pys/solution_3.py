


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        ans = s[0]
        for i in range(1, n):
            if s[i] >= ans[0]:
                ans = s[i] + ans
            else:
                ans = ans + s[i]
        print(ans)


if __name__ == '__main__':
    main()
