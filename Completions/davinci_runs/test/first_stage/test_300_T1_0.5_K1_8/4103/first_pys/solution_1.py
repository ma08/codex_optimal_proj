


def solve(n, b, a, s):
    count = 0
    while n > 0:
        if s[n-1] == 1:
            if b > 0:
                b -= 1
                a += 1
            elif a > 0:
                a -= 1
            else:
                break
        else:
            if a > 0:
                a -= 1
            elif b > 0:
                b -= 1
            else:
                break
        count += 1
        n -= 1
    return count


def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    print(solve(n, b, a, s))


if __name__ == '__main__':
    main()