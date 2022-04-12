

import sys

def main():
    V = int(sys.stdin.readline())
    n = int(V**(1/3))
    while n**3 < V:
        n += 1
    x = n
    y = n
    z = n
    while x*y*z != V and x > 0 and y > 0 and z > 0 and x*y*z > V:
        x -= 1
        y -= 1
        z -= 1
    s = 2*x*y + 2*x*z + 2*y*z
    print(s)

if __name__ == '__main__':
    main()
