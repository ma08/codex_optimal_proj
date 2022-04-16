
from math import sqrt

def main():
    n = int(input())
    for i in range(n):
        m = int(input())
        print(find(m))

def find(m):
    if m == 1:
        return 0
    return int(sqrt(m))

if __name__ == '__main__':
    main()
