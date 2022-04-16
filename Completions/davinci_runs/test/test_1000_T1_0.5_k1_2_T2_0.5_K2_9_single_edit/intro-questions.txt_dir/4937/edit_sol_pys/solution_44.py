
import sys

def main():
    n, a = map(int, sys.stdin.readline().split())
    e = list(map(int, sys.stdin.readline().split())) # input list
    e.sort()
    e.reverse()
    count = 0
    for i in e: # loop through list
        if a >= i: # check if we can use this item
            count += 1
            a -= i
    print(count)

if __name__ == '__main__':
    main()
