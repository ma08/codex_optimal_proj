
def solve(a, b, m, s):
    x = max((s - b) / 2, 0)
    y = max(m - x, 0)
    return (a * x) + (b * y) 

def main():
    a, b = [int(x) for x in raw_input().split()]
    m, s = [int(x) for x in raw_input().split()]
    print solve(a, b, m, s)

if __name__ == '__main__':
    main()
