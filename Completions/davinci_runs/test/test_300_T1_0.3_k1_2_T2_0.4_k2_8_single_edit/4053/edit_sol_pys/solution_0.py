

def main():
    n = int(input())
    prefixes = [0] * n
    suffixes = [0] * n
    for i in range(n):
        prefixes.append(input())
    for i in range(n):
        suffixes.append(input())
    prefixes.sort()
    suffixes.sort()
    for i in range(n):
        print('P', end='') if prefixes[i] else print('S', end='')
    print()

if __name__ == "__main__":
    main()
