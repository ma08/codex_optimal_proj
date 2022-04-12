
def main():
    m, n, t = map(int, input().split()) # m: memory, n: time, t: problem type
    if t == 1:
        if n <= 10: # 10ms
            print("AC")
        else:
            print("TLE")
    elif t == 2:
        if n <= 30: # 30ms
            print("AC")
        else:
            print("TLE")
    elif t == 3:
        if n <= 500: # 500ms
            print("AC")
        else:
            print("TLE")
    elif t == 4:
        if n <= 5000: # 5s
            print("AC")
        else:
            print("TLE")
    elif t == 5:
        if n <= 10000: # 10s
            print("AC")
        else:
            print("TLE")
    elif t == 6:
        if n <= 100000: # 100s
            print("AC")
        else:
            print("TLE")
    elif t == 7:
        if n <= 1000000: # 1000s
            print("AC")
        else:
            print("TLE")

if __name__ == "__main__":
    main()
