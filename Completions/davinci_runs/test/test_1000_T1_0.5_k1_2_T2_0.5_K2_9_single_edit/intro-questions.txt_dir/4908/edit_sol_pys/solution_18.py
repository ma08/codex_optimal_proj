

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    # get input
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    # check for possible operations
    if c == a + b:
        print(str(a) + "+" + str(b) + "=" + str(c))
    elif c == a - b:
        print(str(a) + "-" + str(b) + "=" + str(c))
    elif c == a * b:
        print(str(a) + "*" + str(b) + "=" + str(c))
    elif c == a // b and a % b == 0:
        print(str(a) + "/" + str(b) + "=" + str(c))
    elif c == b // a and b % a == 0:
        print(str(b) + "/" + str(a) + "=" + str(c))
    elif c == a // lcm(a, b) and a % lcm(a, b) == 0:
        print(str(a) + "/" + str(lcm(a, b)) + "=" + str(c))
    elif c == b // lcm(a, b) and b % lcm(a, b) == 0:
        print(str(b) + "/" + str(lcm(a, b)) + "=" + str(c))

if __name__ == "__main__":
    main()
