

def main():
    m, n, t = map(int, input().split())  # m is memory, n is number of lines, t is time limit
    if n > m:  # if number of lines is greater than memory, TLE
        print("TLE")
    elif t == 1:  # if time is 1, TLE
        print("TLE")
    elif t == 2:  # if time is 2, TLE
        print("TLE")
    elif t == 3:  # if time is 3, TLE
        print("TLE")
    elif t == 4:  # if time is 4, TLE
        print("TLE")
    elif t == 5:  # if time is 5, TLE
        print("TLE")
    elif t == 6:  # if time is 6, TLE
        print("TLE")
    else:  # if time is greater than 6, AC
        print("AC")

if __name__ == "__main__":
    main()
