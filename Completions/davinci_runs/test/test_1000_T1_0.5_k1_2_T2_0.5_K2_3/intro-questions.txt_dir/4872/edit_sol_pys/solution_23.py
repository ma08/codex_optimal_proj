

def main():
    n = int(input())
    d = [int(x) for x in input().split()] # list of integers
    i = 1
    cleanups = 1
    while i < n:
        if d[i] - d[i-1] > 20:
            cleanups += 1
            i += 2
        elif i == n-1:
            cleanups += 1
            i += 2
        else:
            i += 2
    print(cleanups)

if __name__ == "__main__":
    main()
