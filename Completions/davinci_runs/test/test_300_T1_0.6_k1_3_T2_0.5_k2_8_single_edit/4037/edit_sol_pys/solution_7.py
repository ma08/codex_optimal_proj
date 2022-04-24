#!/usr/bin/python3


import sys

def main():
    n, r = map(int, sys.stdin.readline().split()) #read first line as int and split
    r = [r]
    for line in sys.stdin: #read every line as int and split
        a, b = map(int, line.split())
        if a > r[-1]: #if a is greater than r (remaining)
            r.append(r[-1])
        else:
            r.append(max(r[-1] - b, 0)) #subtract b from r
    print(len(r) - 1) #print last value

if __name__ == "__main__":
    main()
