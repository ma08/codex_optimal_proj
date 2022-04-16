

import sys
import math

def main():
    K = int(sys.stdin.readline().strip())
    clerks = []
    for i in range(K):
        clerks.append(int(sys.stdin.readline().strip()))
    print(clerks)
    clerks.sort()
    print(clerks)
    max_val = max(clerks)
    print(max_val)
    max_index = clerks.index(max_val)
    print(max_index)
    passes = max_index
    for i in range(max_index+1, K):
        if clerks[i] - clerks[i-1] > 1:
            passes += 1
    print(passes)

if __name__ == '__main__':
    main()
