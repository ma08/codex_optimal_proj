

import sys

def main():
    x = list(map(int, sys.stdin.readline().split()))
    x.append(19)
    x.append(0)
    x.sort()
    print(x[0]*x[1]*x[2]*x[3]*x[4]*x[5]*x[6])

main()
