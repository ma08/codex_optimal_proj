

from math import gcd

def main():
    # get input
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    # check for possible operations
    if c % gcd(a, b) == 0:
        if c // gcd(a, b) == a + b:
            print(str(a) + "+" + str(b) + "=" + str(c))
        elif c // gcd(a, b) == a - b:
            print(str(a) + "-" + str(b) + "=" + str(c))
        elif c // gcd(a, b) == a * b:
            print(str(a) + "*" + str(b) + "=" + str(c))
        elif c // gcd(a, b) == a // b:
            print(str(a) + "/" + str(b) + "=" + str(c))
        elif c // gcd(a, b) == b // a:
            print(str(b) + "/" + str(a) + "=" + str(c))
    elif c == a + b:
        print(str(a) + "+" + str(b) + "=" + str(c))
    elif c == a - b:
        print(str(a) + "-" + str(b) + "=" + str(c))
    elif c == a * b:
        print(str(a) + "*" + str(b) + "=" + str(c))
    elif c == a // b:
        print(str(a) + "/" + str(b) + "=" + str(c))
    elif c == b // a:
        print(str(b) + "/" + str(a) + "=" + str(c))
    elif c == a // lcm(a, b):
        print(str(a) + "/" + str(lcm(a, b)) + "=" + str(c))
    elif c == b // lcm(a, b):
        print(str(b) + "/" + str(lcm(a, b)) + "=" + str(c))

if __name__ == "__main__":
    main()
