#!/usr/bin/python
import sys

def main():
    inp = sys.stdin.read().splitlines()
    cap, n = [int(x) for x in inp[0].split()]
    nums = [[int(x) for x in x.split()] for x in inp[1:]]
    curr = 0
    for i in nums:
        curr -= i[0]
        if curr < 0 or curr + i[1] > cap or (curr + i[1] < cap and i[2] != 0) or (nums.index(i) == len(nums) - 1 and i[2] != 0):
            print("impossible")
            return
        curr += i[1]
    print("possible")

if __name__ == '__main__':
    main()
