
#Solution

#!/usr/bin/env python

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    print arr[len(arr)-2]
