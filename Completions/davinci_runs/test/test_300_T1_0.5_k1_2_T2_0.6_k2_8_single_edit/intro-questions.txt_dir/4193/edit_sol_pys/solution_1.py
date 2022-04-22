
import sys
import math

def read_int():
    return int(sys.stdin.readline())
    
def main():
    # read input
    N = read_int()
    #print(N)
    #print(N * (N + 1) / 2)
    print(math.floor(N * (N + 1) / 2))

if __name__ == "__main__":
    main()
