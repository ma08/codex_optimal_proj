

def solve(a, b, m, s): # a is the price of the cheap ticket, b is the price of the expensive ticket, m is the number of cheap tickets, s is the amount of money I have
    x = s - b # x is the number of expensive tickets I can buy with my money
    if x < 0:
        x = 0
    else:
        x /= 2
    y = m - x # y is the number of cheap tickets I can buy
    if y < 0:
        y = 0
    return (a * y) + (b * x)

def main():
    a, b = [int(x) for x in raw_input().split()]
    m, s = [int(x) for x in raw_input().split()]
    print solve(a, b, m, s)

if __name__ == '__main__':
    main()
