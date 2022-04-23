


def solve(a, b, c, d, e, f, g, h):
    return max(a + d + g, b + e + h, c + f + g) - min(a + d + g, b + e + h, c + f + g)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    h = int(input())
    print(solve(a, b, c, d, e, f, g, h))
