

import sys

def main():
    with open('file.txt', 'r') as f:
        n = f.readline()
        n = int(n)
        a = f.readline()
        a = a.split()
        for i in range(n):
            a[i] = int(a[i])
        print(a)

if __name__ == '__main__':
    main()
