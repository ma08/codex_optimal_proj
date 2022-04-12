

def main():
    m, n, t = map(int, input().split())  # m is memory, n is number of lines, t is time limit.
    if n > m:  # if number of lines is greater than memory.
        print("TLE")
    elif t <= 6:  # if time limit is less than or equal to 6.
        print("TLE")
    else:
        print("AC")

if __name__ == "__main__":
    main()
