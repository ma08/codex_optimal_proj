

def main():
    n = int(input())
    prefixes = []
    suffixes = []
    for _ in range(2*n-2): # 2*n-2
        x = input()
        if len(x)==n-1:
            prefixes.append(x)
        else:
            suffixes.append(x)
    for x in prefixes: # prefixes
        print("P", end="")
    for x in suffixes: # suffixes
        print("S", end="")


if __name__ == '__main__':
    main()
