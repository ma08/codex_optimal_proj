

import sys
import math

def main():
    K = int(sys.stdin.readline().strip())
    clerks = [0]
    for i in range(K):
        clerks.append(int(sys.stdin.readline().strip()))
    clerks.sort()
    max_val = max(clerks)
    max_index = clerks.index(max_val)
    passes = max_index
    for i in range(max_index+1, K):
        if clerks[i] - clerks[i-1] > 1:
            passes += 1
    print(passes+1)

if __name__ == '__main__':
    main()
