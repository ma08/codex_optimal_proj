import math

def t1(n):
    return n * math.factorial(n)

def t2(n):
    return 2 ** n

def t3(n):
    return n * n * n * n

def t4(n):
    return n * n * n

def t5(n):
    return n * n

def t6(n):
    return n * (math.log(n, 2))

def t7(n):
    return n

def main():
    m, n, t = map(int, input().split())
    if t == 1:
        if t1(n) <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 2:
        if t2(n) <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 3:
        if t3(n) <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 4:
        if t4(n) <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 5:
        if t5(n) <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 6:
        if t6(n) <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 7:
        if t7(n) <= m:
            print("AC")
        else:
            print("TLE")

if __name__ == "__main__":
    main()
