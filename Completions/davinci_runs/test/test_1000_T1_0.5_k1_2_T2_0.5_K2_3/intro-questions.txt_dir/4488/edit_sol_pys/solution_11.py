#!/usr/bin/python3

import sys

def main():
    num1 = sys.stdin.readline()
    num2 = sys.stdin.readline()

    if len(num1.rstrip()) > len(num2.rstrip()):
        print("GREATER")
    elif len(num1.rstrip()) < len(num2.rstrip()):
        print("LESS")
    else:
        for i in range(len(num1.rstrip())):
            if int(num1[i].rstrip()) > int(num2[i].rstrip()):
                print("GREATER")
                break
            elif int(num1[i].rstrip()) < int(num2[i].rstrip()):
                print("LESS")
                break
            else:
                if i == len(num1.rstrip())-1:
                    print("EQUAL")

if __name__ == '__main__':
    main()
