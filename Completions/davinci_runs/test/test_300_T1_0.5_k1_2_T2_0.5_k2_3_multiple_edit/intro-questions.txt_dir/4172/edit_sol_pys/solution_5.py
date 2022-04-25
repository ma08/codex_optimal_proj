#!/usr/bin/python3

import sys

def min_moves(a, k):
    a.sort() # sort the array
    moves = 0
    i = 0 # index of the first element
    # iterate over the array
    # while the index of the first element is less than the index of the last element
    j = len(a) - 1
    # if the element is equal to the next element
    while i < j:
        # increment the index of the first element
        if a[i] == a[i + 1]:
            # if the element is equal to the previous element
            i += 1
            # decrement the index of the last element
        elif a[j] == a[j - 1]:
            # if the element is less than the element next to the last element
            j -= 1
        # increment the element
        elif a[i] + 1 < a[j]:
            # decrement the element next to the last element
            a[i] += 1
            # increment the number of moves
            a[j] -= 1
            moves += 1
            # increment the index of the first element
        else:
            # decrement the index of the last element
            i += 1
            j -= 1
    # if the number of unique elements is greater than 1
    if len(set(a)) > 1:
        # increment the number of moves by the difference between the length of the array and k
        moves += len(a) - k
    # return the number of moves
    return moves

def main():
    # read n and k
    n, k = map(int, sys.stdin.readline().strip().split())
    # read the array
    a = list(map(int, sys.stdin.readline().strip().split()))
    # print the minimum number of moves
    print(min_moves(a, k))

if __name__ == '__main__':
    main()
