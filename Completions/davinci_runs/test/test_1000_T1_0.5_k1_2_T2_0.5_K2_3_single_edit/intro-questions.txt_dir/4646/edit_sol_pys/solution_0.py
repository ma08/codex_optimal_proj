
import sys

def solve(a):
    if len(a) % 2 == 0 and a.count(1) % 2:
        # even number of elements
        #   if there are an odd number of odd elements, then we cannot
        #   make the array good
        #   if there are an even number of odd elements, then we can
        #   make the array good
        return -1
    elif len(a) % 2 == 0 and not a.count(1) % 2:
        return 0
    else:
        # odd number of elements
        #   if there are an odd number of odd elements, then we can
        #   make the array good
        #   if there are an even number of odd elements, then we can
        #   make the array good
        return 0

if __name__ == '__main__':

    t = int(sys.stdin.readline())

    for i in range(t):
        n = int(sys.stdin.readline())
        a = map(int, sys.stdin.readline().strip().split())

        print solve(a)
