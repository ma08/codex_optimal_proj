

def solve(a, b, n, s):
    x = s - a
    if x < 0:
        x = 0
    else:
        x = x / 2
    y = n - x
    if y < 0:
        y = 0
    return (a * x) + (b * y)

def main():
    a, b = [int(x) for x in input().split()]
    n, s = [int(x) for x in input().split()]
    print solve(a, b, n, s)

if __name__ == '__main__':
    main()
