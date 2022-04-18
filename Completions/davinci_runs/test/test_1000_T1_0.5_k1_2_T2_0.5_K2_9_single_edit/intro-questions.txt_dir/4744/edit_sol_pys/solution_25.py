

import sys

def main():
    V = int(sys.stdin.readline())
    n = int(V**(1/3))
    while n**3 < V:
        n += 1
    x = n
    y = n
    z = n
        if x*y*z == V:
            break
        x -= 1
        y -= 1
        z -= 1
    s = 2*x*y + 2*x*z + 2*y*z
    print(s)

if __name__ == '__main__':
    main()
