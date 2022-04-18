#!/usr/bin/python
import sys

def main():
    inp = sys.stdin.read().splitlines()
    cap, n = [int(x) for x in inp[0].split()]
    nums = [[int(x) for x in x.split()] for x in inp[1:]]
    curr = 0
    for i in range(n):
        curr -= nums[i][0]
        if curr < 0 or curr + nums[i][1] > cap or (curr + nums[i][1] < cap and nums[i][2] != 0) or (i == n - 1 and nums[i][2] != 0):
            print("impossible")
            return
        curr += nums[i][1]
    print("possible")

if __name__ == '__main__':
    main()
