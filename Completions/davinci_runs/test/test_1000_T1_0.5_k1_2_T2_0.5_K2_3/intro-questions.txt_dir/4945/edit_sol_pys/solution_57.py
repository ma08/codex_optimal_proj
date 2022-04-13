

def solve(a, b, n, s):
    if a * n + b * n <= s:
        return n
    else:
        if a > b:
            return s / b
        else:
            return s / a

def main():
    a, b = [int(x) for x in input().split()]
    n, s = [int(x) for x in input().split()]
    print solve(a, b, n, s)

if __name__ == '__main__':
    main()
