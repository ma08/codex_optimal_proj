
def main():
    n, t = map(int, input().split())
    if t == 1:
        if n <= 10 ** 10:
            print("AC")
        else:
            print("TLE")
    elif t == 2:
        if n <= 10 ** 30:
            print("AC")
        else:
            print("TLE")
    elif t == 3:
        if n <= 10 ** 500:
            print("AC")
        else:
            print("TLE")
    elif t == 4:
        if n <= 10 ** 5000:
            print("AC")
        else:
            print("TLE")
    elif t == 5:
        if n <= 10 ** 10000:
            print("AC")
        else:
            print("TLE")
    elif t == 6:
        if n <= 10 ** 100000:
            print("AC")
        else:
            print("TLE")
    elif t == 7:
        if n <= 10 ** 1000000:
            print("AC")
        else:
            print("TLE")

if __name__ == "__main__":
    main()
