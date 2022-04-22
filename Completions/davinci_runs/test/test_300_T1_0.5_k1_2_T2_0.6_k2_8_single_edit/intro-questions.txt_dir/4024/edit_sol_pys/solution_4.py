

def main():
    n = int(input())
    s = input()
    res = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            if s[i - 1] == 'U':
                res += 2 * (n - i)
            else:
                res += 2 * i - 1
        else:
            if s[i - 1] == 'U':
                res += 1
            else:
                res += 2 * i
    print(res)

if __name__ == '__main__':
    main()
