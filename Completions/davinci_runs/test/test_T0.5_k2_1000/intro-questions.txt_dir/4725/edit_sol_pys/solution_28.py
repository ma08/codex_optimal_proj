
import math
import sys

def main():
    inp = sys.stdin.readline().strip().split()
    n = int(inp[0])
    m = int(inp[1])
    for i in range(m):
        inp = sys.stdin.readline().strip().split()
        a = int(inp[0])
        b = int(inp[1])
        c = int(inp[2])
        print(math.ceil(n / a) * math.ceil(n / b) * math.ceil(n / c))
if __name__ == '__main__':
    main()
