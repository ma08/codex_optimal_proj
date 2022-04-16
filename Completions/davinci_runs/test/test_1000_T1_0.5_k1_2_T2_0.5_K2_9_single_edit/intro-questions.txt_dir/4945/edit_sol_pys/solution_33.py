

def solve(a, b, m, s):
    x = s - a
    if x < 0:
        x = 0
    else:
        x /= 2
    y = m - y
    if y < 0:
        y = 0
    return (a * x) + (b * y)

def main():
    a, b = [int(x) for x in raw_input().split()]
    m, s = [int(x) for x in raw_input().split()]
    print solve(a, b, m, s)

if __name__ == '__main__':
    main()
