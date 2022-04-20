

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
    
    num = 3
    start = 3
    end = 6
    while num < k:
        num += 1
        if num > k:
            return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    num += 1
    if num > k:
        return find(k - (num - 1) + 1)
    
    return find(k - (num - 1) + 1)

if __name__ == '__main__':
    main()
