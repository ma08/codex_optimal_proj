

import math

def t1(n):
    return n * math.factorial(n) <= m * 1000

def t2(n):
    return 2 ** n <= m * 1000

def t3(n):
    return n * n * n * n <= m * 1000

def t4(n):
    return n * n * n <= m * 1000

def t5(n):
    return n * n <= m * 1000

def t6(n):
    return n * (math.log(n, 2)) <= m * 1000

def t7(n):
    return n <= m * 1000

def main():
    m, n, t = map(int, input().split())
    if t == 1:
        if t1(n):
            print("AC")
        else:
            print("TLE")
    elif t == 2:
        if t2(n):
            print("AC")
        else:
            print("TLE")
    elif t == 3:
        if t3(n):
            print("AC")
        else:
            print("TLE")
    elif t == 4:
        if t4(n):
            print("AC")
        else:
            print("TLE")
    elif t == 5:
        if t5(n):
            print("AC")
        else:
            print("TLE")
    elif t == 6:
        if t6(n):
            print("AC")
        else:
            print("TLE")
    elif t == 7:
        if t7(n):
            print("AC")
        else:
            print("TLE")

if __name__ == "__main__":
    main()
