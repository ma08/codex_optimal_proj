


def solve(a, b, c, d):
    if a == c and b == d:
        return ["%d + %d = %d + %d" % (a, b, c, d)]
    elif a > c or (a == c and b > d):
        return ["%d - %d = %d - %d" % (a, b, c, d)]
    elif a*b == c*d:
        return ["%d * %d = %d * %d" % (a, b, c, d)]
    elif a*d == b*c:
        return ["%d / %d = %d / %d" % (a, b, c, d)]
    return ["problems ahead"]


def main():
    a, b, c, d = map(int, input().split())
    for ans in solve(a, b, c, d):
        print(ans)

if __name__ == "__main__":
    main()