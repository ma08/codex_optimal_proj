

import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.append(0) # add 0 to the end of the list
    a.append(n-1) # add n-1 to the end of the list
    a = sorted(a)
    for i in range(n):
        print(a.index(i)+1,end=' ') # print the index of i + 1


main()
