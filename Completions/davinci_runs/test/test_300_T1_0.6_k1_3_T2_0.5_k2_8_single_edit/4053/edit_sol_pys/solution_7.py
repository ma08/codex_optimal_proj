

def main():
    n = int(input())
    prefixes = []
    suffixes = []
    for _ in range(n-1):
        x = input()
        if x[0] not in prefixes:
            prefixes.append(x)
        else:
            suffixes.append(x[len(x)-1])
    for x in prefixes:
        print("P", end=" ")
    for x in suffixes:
        print("S", end=" ")
    print("")


if __name__ == '__main__':
    main()
