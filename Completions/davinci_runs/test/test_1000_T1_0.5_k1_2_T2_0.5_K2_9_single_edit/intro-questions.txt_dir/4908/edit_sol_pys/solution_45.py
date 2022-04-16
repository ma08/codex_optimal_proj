

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    # get input
    inp = raw_input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    # check for possible operations
    if c % gcd(a, b) == 0:
        if c // gcd(a, b) == a + b:
            print(a, "+", b, "=", c)
        elif c // gcd(a, b) == a - b:
            print(a, "-", b, "=", c)
        elif c // gcd(a, b) == a * b:
            print(a, "*", b, "=", c)
        elif c // gcd(a, b) == a // b:
            print(a, "/", b, "=", c)
        elif c // gcd(a, b) == b // a:
            print(b, "/", a, "=", c)
        elif c // gcd(a, b) == a // lcm(a, b):
            print(a, "/", lcm(a, b), "=", c)
        elif c // gcd(a, b) == b // lcm(a, b):
            print(b, "/", lcm(a, b), "=", c)
    elif c == a + b:
        print(a, "+", b, "=", c)
    elif c == a - b:
        print(a, "-", b, "=", c)
    elif c == a * b:
        print(a, "*", b, "=", c)
    elif c == a // b:
        print(a, "/", b, "=", c)
    elif c == b // a:
        print(b, "/", a, "=", c)
    elif c == a // lcm(a, b):
        print(a, "/", lcm(a, b), "=", c)
    elif c == b // lcm(a, b):
        print(b, "/", lcm(a, b), "=", c)

if __name__ == "__main__":
    main()
