

def main():
    n = int(input())
    prefixes = []
    suffixes = []
    for i in range(n):
        prefixes.append(input())
    for i in range(n):
        suffixes.append(input())
    prefixes.sort()
    suffixes.sort()
    for i in range(n):
        print('P', end='')
        print('S', end='')
    print()

if __name__ == "__main__":
    main()