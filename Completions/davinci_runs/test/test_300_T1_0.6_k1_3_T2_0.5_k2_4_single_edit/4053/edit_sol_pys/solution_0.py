

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
    print("P"*len(prefixes) + "S"*len(suffixes))


if __name__ == '__main__':
    main()
