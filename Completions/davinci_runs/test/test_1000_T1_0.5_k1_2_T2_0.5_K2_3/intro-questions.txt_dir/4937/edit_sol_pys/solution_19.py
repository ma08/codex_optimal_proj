

import sys

def inp():
    return sys.stdin.readline()

def main():
    n, a = map(int, sys.stdin.readline().split()) # n: number of envelopes, a: the maximum weight of envelopes
    e = list(map(int, sys.stdin.readline().split())) # e: the list of weight of envelopes
    e.sort() # sorting the list of e
    count = 0
    for i in range(n):
        if a >= e[i]: # if the maximum weight is greater than the weight of envelope
            count += 1 # increase the number of envelopes
            a -= e[i] # decrease the maximum weight
        else:
            break
    print(count)

main()
