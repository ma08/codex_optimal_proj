

def main():
    n = int(input())
    d = [int(x) for x in input().split()] # list comprehension
    i = 1
    cleanups = 0
    while i < n:
        if d[i] - d[i-1] > 20:
            cleanups += 1
            i += 1
        elif i == n-1:
            cleanups += 1
            i += 1
        else:
            i += 1
    print(cleanups)

if __name__ == "__main__":
    main()
