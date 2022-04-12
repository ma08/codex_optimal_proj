

def solve(a, b, m, s): # a is the cost of the first item, b is the cost of the second item, m is the number of the first item, s is the number of the second item
    x = s - b
    if x < 0:
        x = 0
    else:
        x /= 2
    y = m - x
    if y < 0:
        y = 0
    return (a * y) + (b * x)

def main():
    a, b = [int(x) for x in raw_input().split()] # a is the cost of the first item, b is the cost of the second item
    m, s = [int(x) for x in raw_input().split()]
    print solve(a, b, m, s)

if __name__ == '__main__':
    main()
