

import sys

def min_instability(arr):
    min_inst = sys.maxsize
    for i in range(len(arr)):
        inst = max(arr[:i] + arr[i+1:]) - min(arr[:i] + arr[i+1:])
        if inst < min_inst:
            min_inst = inst
    return min_inst

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(min_instability(arr))