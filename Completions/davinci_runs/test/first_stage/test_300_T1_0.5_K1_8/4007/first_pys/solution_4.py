

# Solution

import sys

def main():
    n = int(sys.stdin.readline())
    f = [int(x) for x in sys.stdin.readline().split()]
    g = [0] * n
    for i in range(n):
        if f[i] != 0:
            g[f[i] - 1] = i + 1
    for i in range(n):
        if f[i] == 0:
            for j in range(n):
                if g[j] == 0:
                    g[j] = i + 1
                    break
    print(' '.join(map(str, g)))

if __name__ == "__main__":
    main()