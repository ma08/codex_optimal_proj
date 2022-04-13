
def main():
    s = input()
    n = len(s)

    res = 0
    for i in range(n):
        if s[i] == 'U':
            res += n - i - 1 + 2 * i
        else:
            res += 2 * (n - i - 1) + i

    print(res)

if __name__ == '__main__':
    main()
