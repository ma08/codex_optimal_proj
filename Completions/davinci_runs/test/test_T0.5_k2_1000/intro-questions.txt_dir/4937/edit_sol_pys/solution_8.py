

import sys

def main():
    n, a = map(int, sys.stdin.readline().split()) # n is the number of stones, a is the weight of the boat.
    e = list(map(int, sys.stdin.readline().split())) # e is the list of weights of the stones.
    e.sort() # sort the list
    e.reverse() # reverse the list.
    count = 0
    for i in e: # iterate through the list.
        if a >= i: # if the weight of the boat is greater than the weight of the stone.
            count += 1
            a -= i
    print(count)

if __name__ == '__main__':
    main()
