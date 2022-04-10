

import sys

def main():
    n = int(input())
    prefixes = []
    suffixes = []
    for _ in range(2*n-2):
        s = input()
        if s[0] == 'a':
            prefixes.append(s)
        else:
            suffixes.append(s)
    prefixes.sort()
    suffixes.sort()
    result = ['P' if p in prefixes else 'S' for p in prefixes + suffixes]
    print(''.join(result))

if __name__ == "__main__":
    main()
