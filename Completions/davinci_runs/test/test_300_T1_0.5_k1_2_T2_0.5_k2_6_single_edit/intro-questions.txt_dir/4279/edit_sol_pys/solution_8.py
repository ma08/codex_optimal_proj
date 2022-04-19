

import math

def main():
    # q = int(input())
    # for i in range(q):
    #     k = int(input())
    #     print(find(k))
    print(find(int(input())))

def find(k):
    # if k == 1:
    #     return 1
    # if k == 2:
    #     return 1
    # if k == 3:
    #     return 2
    
    # num = 3
    # start = 3
    # end = 6
    # while num < k:
    #     num += 1
    #     if num == k:
    #         return 1
    #     num += 1
    #     if num == k:
    #         return 1
    #     num += 1
    #     if num == k:
    #         return 2
    #     num += 1
    #     if num == k:
    #         return 3
    #     num += 1
    #     if num == k:
    #         return 3
    #     num += 1
    #     if num == k:
    #         return 4
    #     num += 1
    #     if num == k:
    #         return 4
    #     num += 1
    #     if num == k:
    #         return 5
    #     num += 1
    #     if num == k:
    #         return 5
    #     num += 1
    #     if num == k:
    #         return 6
    
    # return find(k - num + 1)

    return (k - 1) // 2 + 1

if __name__ == '__main__':
    main()
