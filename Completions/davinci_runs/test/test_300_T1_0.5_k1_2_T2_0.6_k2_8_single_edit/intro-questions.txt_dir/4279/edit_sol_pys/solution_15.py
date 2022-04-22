
import math

def main():
    # q = int(input())
    # for i in range(q):
    #     k = int(input())
    #     print(find(k))
    print(find(1))
    print(find(2))
    print(find(3))
    print(find(4))
    print(find(5))
    print(find(6))
    print(find(7))
    print(find(8))
    print(find(9))
    print(find(10))
    print(find(11))
    print(find(12))
    print(find(13))
    print(find(14))
    print(find(15))
    print(find(16))
    print(find(17))
    print(find(18))
    print(find(19))
    print(find(20))
    print(find(21))
    print(find(22))
    print(find(23))
    print(find(24))
    print(find(25))

def find(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    if k == 3:
        return 2
    num = 0
    start = 3
    end = 6
    while num <= k:
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        num += 1
        if num > k:
            return find(k - start)
        start = end
        end += 6

if __name__ == '__main__':
    main()
