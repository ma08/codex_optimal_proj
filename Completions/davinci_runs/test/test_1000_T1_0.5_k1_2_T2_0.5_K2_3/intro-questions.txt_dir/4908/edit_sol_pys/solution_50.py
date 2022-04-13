

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    # get input
    a, b, c = map(int, input().split())
    # check for possible operation
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
        elif c // gcd(a, b) == a // lcm(a, b):
            print(str(a) + "/" + str(lcm(a, b)) + "=" + str(c))
        elif c // gcd(a, b) == b // lcm(a, b):
            print(str(b) + "/" + str(lcm(a, b)) + "=" + str(c))
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
