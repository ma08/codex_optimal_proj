

import sys

def main():
    V = int(sys.stdin.readline())
    n = int(V**(1/3))
    while n**3 < V:
        n += 1
    y = 1
    z = 1
    while n*y*z != V:
        y += 1
        z += 1
    s = 2*n*y + 2*n*z + 2*y*z
    print(s)

if __name__ == '__main__':
    main()
