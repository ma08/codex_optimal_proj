#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        lines.append(sys.stdin.readline().strip().split())
    lineCount = 1
    for line in lines:
        if line[-2] != "->":  # check whether the last two elements are "->"
            print(lineCount)
            break
        else:
            for i in range(len(line)-2):  # check whether the other elements have appeared before
                if line[i] not in lines[:lineCount-1]:  # if yes, print the line number and exit
                    print(lineCount)
                    break
        lineCount += 1
    else:  # if no errors are found, print "correct"
        print("correct")

main()
