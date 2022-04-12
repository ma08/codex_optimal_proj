

import sys

def main():
    S, C, K = [int(i) for i in sys.stdin.readline().split()] # S is the number of socks, C is the number of colors, K is the maximum difference.
    D = [int(i) for i in sys.stdin.readline().split()] # D is the color of the socks.
    D.sort() # sort the socks by color.
    i = 0
    count = 0
    while i < S:
        count += 1
        j = i + 1
        while j < S and D[j] - D[i] <= K: # if the difference between the color of the socks is less than or equal to K, put them in the same machine.
            j += 1
        i = j
    print(count)

if __name__ == '__main__':
    main()
