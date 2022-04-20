

def main():
    n = int(input())
    prefixes = []
    suffixes = []
    for _ in range(2*n-2):
        x = input()
        if x not in prefixes:
            prefixes.append(x)
        else:
            suffixes.append(x)
    for x in prefixes:
        print("P")
    for x in suffixes:
        print("S")


if __name__ == '__main__':
    main()
