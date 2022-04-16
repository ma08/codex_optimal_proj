

def main():
    m, n, t = map(int, input().split())
    if n > m or t == 1 or t == 2 or t == 3 or t == 4 or t == 5 or t == 6:
        print("TLE")
    else:
        print("AC")

if __name__ == "__main__":
    main()
