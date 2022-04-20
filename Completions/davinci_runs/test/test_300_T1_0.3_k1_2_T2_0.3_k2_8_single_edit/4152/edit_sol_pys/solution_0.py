

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()] # read the input
    a.sort()
    if n == 1:
        print(1)
        return
    i = 0 # initialize the pointers
    j = n-1
    count = 0
    while i < j:
        if a[i] + a[j] == 2**int(math.log(a[i]+a[j],2)): # if the sum is a power of 2
            i += 1
            j -= 1
        elif a[i] + a[j] > 2**int(math.log(a[i]+a[j],2)): # if the sum is greater than the power of 2
            j -= 1
            count += 1
        else: # if the sum is less than the power of 2
            i += 1
            count += 1
    if i == j: # if there is an odd number of elements
        count += 1
    print(count)

if __name__ == "__main__":
    main()
