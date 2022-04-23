
import math
import math

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(find(k))

def find(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    if k == 3:
        return 2
    
    num = 4
    while num < k:
        num *= 2
    
    return find(k - num / 2 + 1)

if __name__ == '__main__':
    main()
