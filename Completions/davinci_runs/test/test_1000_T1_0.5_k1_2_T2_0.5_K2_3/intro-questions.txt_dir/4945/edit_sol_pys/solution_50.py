

def solve(a, b, n, s):
    x = s // a
    y = n - x
    return (a * x) + (b * y) if y >= 0 else -1

def main():
    a, b = [int(x) for x in raw_input().split()]
    n, s = [int(x) for x in raw_input().split()]
    print solve(a, b, n, s)

if __name__ == '__main__':
    main()
