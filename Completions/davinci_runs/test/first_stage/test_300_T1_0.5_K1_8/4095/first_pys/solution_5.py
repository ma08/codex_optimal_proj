

import sys

def main():
    lines = sys.stdin.readlines()
    n, m = map(int, lines[0].strip().split())
    p = map(int, lines[1].strip().split())

    #calculate the number of elements in the permutation that are less than m
    count = 0
    for i in range(n):
        if p[i] < m:
            count += 1

    #if m is in the permutation, then the number of elements that are equal to m is also added to count
    if m in p:
        count += 1

    #if count is in the middle of the permutation, then all the possible pairs of indices that have m as the median are given by:
    #(1, count), (2, count), ..., (count-1, count), (count, count), (count, count+1), ..., (count, n)
    if count == m:
        print count * (n-count+1)
    #if count is less than m, then all the possible pairs of indices that have m as the median are given by:
    #(count+1, count+1), (count+1, count+2), ..., (count+1, n)
    elif count < m:
        print (n-count)
    #if count is greater than m, then all the possible pairs of indices that have m as the median are given by:
    #(1, count-1), (2, count-1), ..., (count-1, count-1)
    else:
        print count-1


if __name__ == "__main__":
    main()