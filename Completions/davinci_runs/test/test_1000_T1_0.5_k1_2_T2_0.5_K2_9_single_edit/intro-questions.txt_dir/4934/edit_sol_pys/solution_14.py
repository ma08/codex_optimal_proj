

import sys
import random
import math

random.seed()

def gen_list(size):
    return [random.randint(0, size) for i in range(size)]

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break 

    return result

def merge_sort(list):
    if len(list) < 2:
        return list

    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])

    return merge(left, right)

def main():
    num_list = gen_list(10)
    print(num_list)
    print(merge_sort(num_list))

if __name__ == '__main__':
    main()
