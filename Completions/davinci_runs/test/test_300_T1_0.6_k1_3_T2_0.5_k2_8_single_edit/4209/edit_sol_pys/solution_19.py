

import sys

# TODO: Timeout

def find_max_block_set(arr):
    max_block_count = 1
    max_block_set = [[]]
    for i in range(len(arr)):
        curr_sum = arr[i]
        curr_block_set = [i+1]
        for j in range(i+1, len(arr)):
            curr_sum += arr[j]
            if curr_sum <= 0:
                curr_block_set.append(j+1)
                if len(curr_block_set) > max_block_count:
                    max_block_count = len(curr_block_set)
                    max_block_set = [curr_block_set]
                elif len(curr_block_set) == max_block_count:
                    max_block_set.append(curr_block_set)
                curr_sum = 0
                curr_block_set = [i+1]
    return max_block_set

def find_max_block_set_2(arr):
    max_block_count = 0
    max_block_set = []
    for i in range(len(arr)):
        curr_sum = arr[i]
        curr_block_set = []
        for j in range(i+1, len(arr)):
            curr_sum += arr[j]
            if curr_sum <= 0:
                curr_block_set.append(j+1)
                if len(curr_block_set) > max_block_count:
                    max_block_count = len(curr_block_set)
                    max_block_set = [curr_block_set]
                elif len(curr_block_set) == max_block_count:
                    max_block_set.append(curr_block_set)
                curr_sum = 0
                curr_block_set = [i+1]
    return max_block_set

def find_max_block_set_3(arr):
    max_block_count = 0
    max_block_set = []
    for i in range(len(arr)):
        curr_block_count = 1
        curr_sum = arr[i]
        curr_block_set = []
        for j in range(i+1, len(arr)):
            curr_sum += arr[j]
            if curr_sum <= 0:
                curr_block_set.append(j+1)
                curr_block_count += 1
                if curr_block_count > max_block_count:
                    max_block_count = curr_block_count
                    max_block_set = [curr_block_set]
                elif curr_block_count == max_block_count:
                    max_block_set.append(curr_block_set)
                curr_sum = 0
                curr_block_set = [i+1]
    return max_block_set

def find_max_block_set_4(arr):
    max_block_count = 0
    max_block_set = []
    for i in range(len(arr)):
        curr_block_count = 1
        curr_sum = arr[i]
        curr_block_set = []
        for j in range(i+1, len(arr)):
            curr_sum += arr[j]
            if curr_sum <= 0:
                curr_block_set.append(j+1)
                curr_block_count += 1
                if curr_block_count > max_block_count:
                    max_block_count = curr_block_count
                    max_block_set = [curr_block_set]
                elif curr_block_count == max_block_count:
                    max_block_set.append(curr_block_set)
                curr_sum = 0
                curr_block_set = [i+1]
    return max_block_set


def main():
    arr = [int(i) for i in input().split()]
    max_block_set = find_max_block_set_4(arr)
    print(len(max_block_set))
    for block in max_block_set:
        print(block[0], block[-1])

if __name__ == "__main__":
    main()
