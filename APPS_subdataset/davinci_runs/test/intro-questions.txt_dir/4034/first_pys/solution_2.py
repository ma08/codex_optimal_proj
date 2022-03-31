


def main():
    n = int(input())
    s = input().strip()
    if len(s) != n:
        raise ValueError('invalid input')

    if s == s[::-1]:
        ans = '0' * n
    else:
        ans = [0] * n
        for i in range(1, n):
            if s[i] == s[i - 1]:
                ans[i] = ans[i - 1] ^ 1
            else:
                ans[i] = ans[i - 1]

    print('YES')
    print(''.join(map(str, ans)))


if __name__ == "__main__":
    main()