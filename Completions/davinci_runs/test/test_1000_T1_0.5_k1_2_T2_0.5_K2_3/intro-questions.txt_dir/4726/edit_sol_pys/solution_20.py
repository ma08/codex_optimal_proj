import math

def main():
    m, n, t = map(int, input().split())
    if t == 1:
        if m < n:
            print("TLE")
        else:
            print("AC")
    if t == 2:
        if m < 2 ** n:
            print("TLE")
        else:
            print("AC")
    if t == 3:
        if m < n ** 4:
            print("TLE")
        else:
            print("AC")
    if t == 4:
        if m < n ** 3:
            print("TLE")
        else:
            print("AC")
    if t == 5:
        if m < n ** 2:
            print("TLE")
        else:
            print("AC")
    if t == 6:
        if m < n * math.log2(n):
            print("TLE")
        else:
            print("AC")
    if t == 7:
        if m < n:
            print("TLE")
        else:
            print("AC")

if __name__ == "__main__":
    main()
