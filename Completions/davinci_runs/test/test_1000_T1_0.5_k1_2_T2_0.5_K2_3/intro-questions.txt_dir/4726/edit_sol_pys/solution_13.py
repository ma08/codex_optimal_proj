
import sys

    sys.setrecursionlimit(10**6)
def main():
    m, n, t = [int(x) for x in sys.stdin.readline().split()]
    if t == 1:
        if n <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 2:
        if 2**n <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 3:
        if n**4 <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 4:
        if n**3 <= m: 
            print("AC")
        else:
            print("TLE")
    elif t == 5:
        if n**2 <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 6:
        if n*(n**(1/2)) <= m:
            print("AC")
        else:
            print("TLE")
    elif t == 7:
        if n <= m:
            print("AC")
        else:
            print("TLE")

if __name__ == '__main__':
    main()
