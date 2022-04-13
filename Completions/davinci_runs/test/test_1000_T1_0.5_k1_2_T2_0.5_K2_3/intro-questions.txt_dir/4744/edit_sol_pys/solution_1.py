

import sys

def main():
    volume = int(sys.stdin.readline())
    n = int(volume**(1/3))
    while n**3 < volume:
        n += 1
    x = n
    y = n
    z = n
        if x*y*z == volume:
            break
        x -= 1
        y -= 1
        z -= 1
    s = 2*x*y + 2*x*z + 2*y*z
    print(s)

if __name__ == '__main__':
    main()
