

import sys

def main():
    v = list(map(int, sys.stdin.readline().split()))
    v.append(19) # for the first digit
    v.append(0) # for the last digit
    v.sort()
    print(v[0]*v[1]*v[2]*v[3]*v[4]*v[5]*v[6]) # print the result

main()
