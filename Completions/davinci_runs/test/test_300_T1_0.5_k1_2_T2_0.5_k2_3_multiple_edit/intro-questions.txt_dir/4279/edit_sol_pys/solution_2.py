

import math

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(find(k))

def find(k):
    if k % 2 == 1:
        return k // 2
    return (k // 2) + 1

if __name__ == '__main__':
    main()
