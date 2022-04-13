
def solve(a, b, m, s):
    x = s - b
    x = max(x, 0)
    x /= 2
    y = m - x
    y = max(y, 0)
    return (a * x) + (b * y)

def main():
    a, b = [int(x) for x in raw_input().split()]
    m, s = [int(x) for x in raw_input().split()]
    print solve(a, b, m, s)

if __name__ == '__main__':
    main()
