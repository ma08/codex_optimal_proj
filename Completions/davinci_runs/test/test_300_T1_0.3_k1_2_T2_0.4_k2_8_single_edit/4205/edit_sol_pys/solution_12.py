

import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    #print(N, K, A)

    # if the number of elements that are not in the correct position is less than K, it is possible to sort A
    # by swapping the elements that are not in the correct position K times.
    # if the number of elements that are not in the correct position is K or more, it is impossible to sort A
    # by swapping the elements that are not in the correct position K times.
    count = 0 # the number of elements that are not in the correct position
    for i in range(N): # for each element in A
        if A[i] != i + 1: # if the element is not in the correct position
            count += 1 # increment count
    if count <= K: # if the number of elements that are not in the correct position is less than or equal to K
        print("YES") # it is possible to sort A by swapping the elements that are not in the correct position K times
    else: # if the number of elements that are not in the correct position is more than K
        print("NO") # it is impossible to sort A by swapping the elements that are not in the correct position K times

if __name__ == '__main__':
    main()
