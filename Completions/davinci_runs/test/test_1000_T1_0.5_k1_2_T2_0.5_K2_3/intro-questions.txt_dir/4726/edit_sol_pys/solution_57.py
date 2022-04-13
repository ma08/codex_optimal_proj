
def main():
    m, n, t = map(int, input().split())
    if t == 1:
        if m <= 10:
            print("AC")
        else:
            print("TLE")
    elif t == 2:
        if m <= 10000:
            print("AC")
        else:
            print("TLE")
    elif t == 3:
        if m <= 3000:
            print("AC")
        else:
            print("TLE")
    elif t == 4:
        if m <= 100000:
            print("AC")
        else:
            print("TLE")
    elif t == 5:
        if m <= 300000:
            print("AC")
        else:
            print("TLE")
    elif t == 6:
        if m <= 1000000:
            print("AC")
        else:
            print("TLE")
    elif t == 7:
        if m <= 10000000:
            print("AC")
        else:
            print("TLE")

if __name__ == "__main__":
    main()
