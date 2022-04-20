

import sys

def main():
    # get input
    n = int(sys.stdin.readline())
    diff = [int(x) for x in sys.stdin.readline().split()]

    # sort the list
    diff.sort()

    # get the number of problems for ARCs
    n_arc = n//2
    n_abc = n//2

    # get the target difficulty
    target = diff[n_arc]

    # count the number of choices of K
    count = 0
    for i in range(n):
        if diff[i] >= target:
            count += 1

    print(count)

if __name__ == '__main__':
    main()