

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    i = 1
    clean_ups = 0
    while i < n:
        if d[i] - d[i-1] > 20:
            clean_ups += 1
            i += 1
        elif i == n-1:
            clean_ups += 1
            i += 1
        else:
            i += 1
    print(clean_ups)

if __name__ == "__main__":
    main()
