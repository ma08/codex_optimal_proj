
def main():
    m, n, t = map(int, input().split())
    if t == 1:
        if n <= 10:
            print("AC")
        else:
            print("TLE")
    elif t == 2:
        if n <= 30:
            print("AC")
        else:
            print("TLE")
    elif t == 3:
        if n <= 500:
            print("AC")
        else:
            print("TLE")
    elif t == 4:
        if n <= 5000:
            print("AC")
        else:
            print("TLE")
    elif t == 5:
        if n <= 10000:
            print("AC")
        else:
            print("TLE")
    elif t == 6:
        if n <= 100000:
            print("AC")
        else:
            print("TLE")
    elif t == 7:
        if n <= 1000000:
            print("AC")
        else:
            print("TLE")

if __name__ == "__main__":
    main()
