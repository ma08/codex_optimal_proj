

import sys

def main():
    v = list(map(int, sys.stdin.readline().split()))[:6]
    v.extend([20, 0])
    v.sort() 
    print(v[0]*v[1]*v[2]*v[3]*v[4]*v[5]*v[6]) 

main()
