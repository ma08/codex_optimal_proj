

import sys

def main():
    f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    n, k = [int(x) for x in f.readline().split()]
    a = [int(x) for x in f.readline().split()]
    # TODO: solve the problem
    # print(n, k)
    # print(a)
    
    # TODO: output the result
    # print(n, k)
    # print(a)

if __name__ == "__main__":
    main()