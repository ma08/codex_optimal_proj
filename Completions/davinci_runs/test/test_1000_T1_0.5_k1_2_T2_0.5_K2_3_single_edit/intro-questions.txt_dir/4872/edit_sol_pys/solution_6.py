

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    i = 0
    cleanups = 0
    while i < n-1:
        if d[i] - d[i-1] > 20:
            cleanups += 1
            i += 1
        else:
            i += 1
    print(cleanups)

if __name__ == "__main__":
    main()
