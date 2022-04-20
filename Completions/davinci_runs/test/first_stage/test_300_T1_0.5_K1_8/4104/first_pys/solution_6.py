

#!/usr/bin/env python

import sys

def main():
    nums = [int(x) for x in sys.stdin.readline().split('+')]
    total = 0
    for i in xrange(len(nums)):
        total += nums[i]
    print total

if __name__ == '__main__':
    main()