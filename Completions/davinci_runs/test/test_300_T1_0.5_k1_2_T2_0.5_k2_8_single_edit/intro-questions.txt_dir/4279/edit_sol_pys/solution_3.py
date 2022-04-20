

import math

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(find(k))

def find(k):
    return find(k - num + 1) 

if __name__ == '__main__':
    main()
