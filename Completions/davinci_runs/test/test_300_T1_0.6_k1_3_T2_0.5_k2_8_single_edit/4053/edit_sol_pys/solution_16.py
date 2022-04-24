

def main():
    n = int(input())
    prefixes = []
    suffixes = []
    for _ in range(2*n-2):
        x = input()
        if len(x) == n-1:
            prefixes.append(x)
        else:
            suffixes.append(x)

    for i in range(n-1):
        if prefixes[i] in suffixes[i]:
            print("P", end="")
        else:
            print("S", end="")


if __name__ == '__main__':
    main()
