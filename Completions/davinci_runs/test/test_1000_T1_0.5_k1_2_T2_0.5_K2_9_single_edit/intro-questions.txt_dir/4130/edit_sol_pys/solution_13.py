

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort() # sort the weights
    ans = 1 # the answer is at least 1
    prev = a[0] # the previous weight
    for i in range(1, n): # go over the weights
        if a[i] == prev: # if the current weight is the same as the previous one, increase it by one
            prev += 1
        elif a[i] > prev + 1: # if the current weight is bigger than the previous one by more than one, decrease it by one
            prev = a[i] - 1
        ans += 1 # increase the answer
    print(ans) # print the answer

if __name__ == '__main__':
    main()
