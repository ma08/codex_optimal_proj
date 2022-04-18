

def main():
    L, R = map(int, input().split())
    if L == R:
        print("Even %d" % (L + R))
    elif L > R:
        print("Odd %d" % (2 * L))
    else:
        print("Odd %d" % (2 * R))

if __name__ == "__main__":
    main()
