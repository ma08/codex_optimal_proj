#!/usr/bin/python3

import sys

def main():
    num1 = sys.stdin.readline().rstrip().split()
    num2 = sys.stdin.readline().rstrip().split()

    if num1[0] > num2[0]:
        print("GREATER")
    elif num1[0] < num2[0]:
        print("LESS")
    else:
        for i in range(len(num1[1])):
            if int(num1[1][i]) > int(num2[1][i]):
                print("GREATER")
                break
            elif int(num1[1][i]) < int(num2[1][i]):
                print("LESS")
                break
            else:
                if i == len(num1[1])-1:
                    print("EQUAL")

if __name__ == '__main__':
    main()
