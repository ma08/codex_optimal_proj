


def find_cleanups(d):
    i = 1
    cleanups = 0
    while i < len(d):
        if d[i] - d[i-1] > 20:
            cleanups += 1
            i += 1
        elif i == len(d)-1:
            cleanups += 1
            i += 1
        else:
            i += 1
    return cleanups


def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    cleanups = find_cleanups(d)

    print(cleanups)

if __name__ == "__main__":
    main()
