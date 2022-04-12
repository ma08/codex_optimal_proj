

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    # get inputs
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    # check for possible operations 
    if c % gcd(a, b) == 0: # check for division
        if c // gcd(a, b) == a + b: # check for addition
            print(str(a) + "+" + str(b) + "=" + str(c))
        elif c // gcd(a, b) == a - b: # check for subtraction
            print(str(a) + "-" + str(b) + "=" + str(c))
        elif c // gcd(a, b) == a * b: # check for multiplication
            print(str(a) + "*" + str(b) + "=" + str(c))
        elif c // gcd(a, b) == a // b: # check for division
            print(str(a) + "/" + str(b) + "=" + str(c))
        elif c // gcd(a, b) == b // a: # check for division
            print(str(b) + "/" + str(a) + "=" + str(c))
        elif c // gcd(a, b) == a // lcm(a, b): # check for division
            print(str(a) + "/" + str(lcm(a, b)) + "=" + str(c))
        elif c // gcd(a, b) == b // lcm(a, b): # check for division
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
