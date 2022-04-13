

import sys

def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N, 1000): # loop through numbers from N to 1000
        if (i % 111) == 0: # if the remainder is 0, then it is divisible by 111 (i.e. 111, 222, 333, ...)
            print(i)
            break

if __name__ == "__main__":
    main()
