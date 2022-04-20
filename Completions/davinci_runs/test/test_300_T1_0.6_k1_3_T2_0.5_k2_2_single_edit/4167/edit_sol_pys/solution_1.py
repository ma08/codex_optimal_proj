#!/bin/python3

import sys

def get_total_x(a, b):
    # Write your code here
    count = 0
    for i in range(a[len(a)-1], b[0]+1):
        flag = True
        for j in range(len(a)):
            if i % a[j] != 0:
                flag = False
                break
        if flag:
            for j in range(len(b)):
                if b[j] % i != 0:
                    flag = False
                    break
        if flag:
            count += 1
    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = get_total_x(arr, brr)
    print(str(total) + '\n')
