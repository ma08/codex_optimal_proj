

import sys

def inp():
    return int(sys.stdin.readline())

def main():
    n, a = map(int, sys.stdin.readline().split())
    e = list(map(int, sys.stdin.readline().split()))
    e.sort()
    #print(e) 
    count = 0 # count how many people can be saved
    for i in range(n):
        if a >= e[i]: # if the energy is greater than the energy of the i-th person
            count += 1
            a -= e[i]
        else: # if the energy is less than the energy of the i-th person
            break
    print(count)

main()
