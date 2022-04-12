

def main():
    m, n, t = map(int, input().split())
    if t == 1:
        if n <= 10 and m <= 10:
            print("AC")
        else:
            print("TLE")
    elif t == 2:
        if n <= 30 and m <= 10:
            print("AC")
        else:
            print("TLE")
    elif t == 3:
        if n <= 500 and m <= 10:
            print("AC")
        else:
            print("TLE")
    elif t == 4:
        if n <= 5000 and m <= 10:
            print("AC")
        else:
            print("TLE")
    elif t == 5:
        if n <= 10000 and m <= 10:
            print("AC")
        else:
            print("TLE")
    elif t == 6:
        if n <= 100000 and m <= 10:
            print("AC")
        else:
            print("TLE")
    elif t == 7:
        if n <= 1000000 and m <= 10:
            print("AC")
        else:
            print("TLE")

if __name__ == "__main__":
    main()
