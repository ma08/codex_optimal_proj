

import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    #print(N, p)

    # if the number of elements that are not in the correct position is less than 2, it is possible to sort p
    # by swapping the elements that are not in the correct position.
    # if the number of elements that are not in the correct position is 2 or more, it is impossible to sort p
    # by swapping the elements that are not in the correct position.
    count = 0
    for i in range(N):
        if A[i] != i + 1:
            count += 1
    if count < 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
