
import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert len(a) == n

    left = [0] * n   # array of length n with all 0s
    right = [0] * n  # array of length n with all 0s

    left[0] = 1   # the first element in left array will be 1
    right[n-1] = 1

    for i in range(1, n):
        left[i] = left[i-1]  # left[i] will be equal to left[i-1]
        if a[i] > a[i-1]:
            left[i] += 1  # if a[i] is greater than a[i-1], left[i] will be increased by 1

    for i in range(n-2, -1, -1):
        right[i] = right[i+1]  # right[i] will be equal to right[i+1]
        if a[i] < a[i+1]:
            right[i] += 1  # if a[i] is less than a[i+1], right[i] will be increased by 1

    max_len = 0  # max_len starts with 0
    max_len_idx = -1  # max_len_idx starts with -1
    for i in range(n):
        if left[i] + right[i] - 1 > max_len:  # if left[i] + right[i] - 1 is greater than max_len
            max_len = left[i] + right[i] - 1  # max_len will be equal to left[i] + right[i] - 1
            max_len_idx = i  # max_len_idx will be equal to i

    print(max_len)
    seq = []
    for i in range(max_len_idx, -1, -1):  # for i in range max_len_idx to -1
        if left[i] == 1:  # if left[i] is equal to 1
            break
        seq.append('L')  # left[i] will be appended to seq

    for i in range(max_len_idx, n):  # for i in range max_len_idx to n
        if right[i] == 1:  # if right[i] is equal to 1
            break
        seq.append('R')  # right[i] will be appended to seq

    print(''.join(seq))  # seq will be printed without spaces

if __name__ == '__main__':
    main()
