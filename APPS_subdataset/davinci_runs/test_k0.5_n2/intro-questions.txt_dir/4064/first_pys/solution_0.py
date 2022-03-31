


def solve(n, h, l, r, a):
    res = 0
    if l <= 0 and r >= h - 1:
        res = n
    elif l <= 0:
        res = 1
        while r < h - 1:
            if r + 1 in a:
                res += 1
                r += 1
            else:
                break
        if r + 1 in a:
            res += 1
        else:
            res += 1
    elif r >= h - 1:
        res = 1
        while l > 0:
            if l - 1 in a:
                res += 1
                l -= 1
            else:
                break
        if l - 1 in a:
            res += 1
        else:
            res += 1
    else:
        res = 1
        while l > 0:
            if l - 1 in a:
                res += 1
                l -= 1
            else:
                break
        if l - 1 in a:
            res += 1
        else:
            res += 1
        while r < h - 1:
            if r + 1 in a:
                res += 1
                r += 1
            else:
                break
        if r + 1 in a:
            res += 1
        else:
            res += 1
    return res


def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, h, l, r, a))


if __name__ == "__main__":
    main()