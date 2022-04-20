

def main():
    n = int(input())
    s = input()

    # a[i][j] = number of regular bracket sequences of length 2i containing s[:j] as a substring
    a = [[0] * (len(s) + 1) for _ in range(n + 1)]
    a[0][0] = 1

    for i in range(n):
        for j in range(len(s) + 1):
            if a[i][j] == 0:
                continue

            # case 1: add ')' to the end of s[:j]
            if j < len(s) and s[j] == ')':
                a[i + 1][j + 1] += a[i][j]

            # case 2: add '()' to the end of s[:j]
            if j < len(s) - 1 and s[j] == '(' and s[j + 1] == ')':
                a[i + 1][j + 2] += a[i][j]

            # case 3: add '(' to the end of s[:j]
            a[i + 1][j] += a[i][j] * (i + 1)

    print(a[n][len(s)] % 1000000007)


if __name__ == '__main__':
    main()