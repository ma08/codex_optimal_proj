

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    # get input
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    # check for possible operation
    if c % gcd(a, b) == 0: # check if c is a multiple of a and b
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
    elif c == a + b: # check for addition
        print(str(a) + "+" + str(b) + "=" + str(c))
    elif c == a - b: # check for subtraction
        print(str(a) + "-" + str(b) + "=" + str(c))
    elif c == a * b: # check for multiplication
        print(str(a) + "*" + str(b) + "=" + str(c))
    elif c == a // b: # check for division
        print(str(a) + "/" + str(b) + "=" + str(c))
    elif c == b // a: # check for division
        print(str(b) + "/" + str(a) + "=" + str(c))
    elif c == a // lcm(a, b): # check for division
        print(str(a) + "/" + str(lcm(a, b)) + "=" + str(c))
    elif c == b // lcm(a, b): # check for division
        print(str(b) + "/" + str(lcm(a, b)) + "=" + str(c))

if __name__ == "__main__":
    main()
