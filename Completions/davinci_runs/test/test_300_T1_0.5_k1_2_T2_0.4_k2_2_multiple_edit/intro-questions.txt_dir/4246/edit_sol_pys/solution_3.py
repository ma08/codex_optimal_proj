#!/usr/bin/env python3

import sys

def main():
    forecast = sys.stdin.readline().strip().split()
    actual = sys.stdin.readline().strip().split()

    correct = 0
    for i in range(len(forecast)):
        if forecast[i] == actual[i]:
            correct += 1
    print(correct)

if __name__ == '__main__':
    main()
