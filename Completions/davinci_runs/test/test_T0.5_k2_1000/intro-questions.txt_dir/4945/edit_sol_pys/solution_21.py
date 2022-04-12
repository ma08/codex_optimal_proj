

def solve(a, b, m, s): # a is the cost of a single ticket, b is the cost of a pair of tickets, m is the number of single tickets, s is the number of pairs of tickets
    x = s - b # x is the number of pairs of tickets that can be bought
    if x < 0:
        x = 0
    else:
        x *= 2 # x is doubled because each pair of tickets is equivalent to 2 single tickets
    y = m - x # y is the number of single tickets that can be bought
    if y < 0:
        y = 0
    return (a * x) + (b * y)

def main():
    a, b = [int(x) for x in raw_input().split()]
    m, s = [int(x) for x in raw_input().split()]
    print solve(a, b, m, s)

if __name__ == '__main__':
    main()
