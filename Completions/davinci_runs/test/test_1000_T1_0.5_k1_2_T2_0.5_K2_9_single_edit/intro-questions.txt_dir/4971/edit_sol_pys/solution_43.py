
import sys
import math

def main():
    m = int(sys.stdin.readline().strip())
    x = -1
    for a in range(1,math.ceil(m**(1/3))):
        for b in range(1,math.ceil(m**(1/3))):
            if (a**3 + b**3) <= m:
                x = max(x,a**3 + b**3)
    if x == -1:
        print("none")
    else:
        print(x)
main()
