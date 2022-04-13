

import sys

def main():
    v = list(map(int, sys.stdin.readline().split()))
    v.append(20) #add 20 to the list
    v.append(0) #add 0 to the list
    v.sort()
    print(v[0]*v[1]*v[2]*v[3]*v[4]*v[5]*v[6]) #print the product of all the elements in the list

main()
