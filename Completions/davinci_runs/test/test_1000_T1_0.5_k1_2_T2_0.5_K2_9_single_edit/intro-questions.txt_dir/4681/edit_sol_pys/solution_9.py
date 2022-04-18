

import sys

def main():
    n = int(input)
    l = []
    for i in range(n-1):
        l.append(l[i] + l[i-1])
    print(l[n-1])

if __name__ == '__main__':
    main()
