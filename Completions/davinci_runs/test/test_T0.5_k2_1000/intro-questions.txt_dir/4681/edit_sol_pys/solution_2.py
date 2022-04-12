

import sys

def main():
    n = int(input())
    l = [1, 1, 2]
    for i in range(n):
        l.append(l[i] + l[i+1] + l[i+2])
    print(l[n])

if __name__ == '__main__':
    main()
