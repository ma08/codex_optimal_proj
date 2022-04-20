

def main():
    n = int(input())
    prefixes = [0] * n
    suffixes = [0] * n
    for i in range(n):
        prefixes[i] = input()
    for i in range(n):
        suffixes[i] = input()
    prefixes.sort()
    suffixes.sort()
    for i in range(n):
        print('P', end='')
        print('S', end='')
    print()

if __name__ == "__main__":
    main()
