

#Solution:

import sys

def main():
    s=int(input())
    print(s,":")
    for i in range(2,s+1):
        for j in range(1,i):
            if 2*j+i<=s and s%(i+j)==0:
                print(i,",",j)

main()
