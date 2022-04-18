

import sys

def main():
    n = int(input())
    l = [0, 1, 2]
    for i in range(3, n+1):
        l.append(l[i-1] + l[i-2])
    print(l[n-1])

if __name__ == '__main__':
    main()
